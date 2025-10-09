"""
Paris-SCM Router: Lightweight Transformer for legal expert routing
Based on Paris decentralized diffusion model architecture
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Tuple, Optional
import numpy as np


class LegalRouterMini(nn.Module):
    """
    Lightweight router for Paris-SCM legal experts.
    
    Routes legal queries to appropriate expert(s) based on:
    - Semantic content (embeddings)
    - Abstraction level (norm/principle/case/policy)
    - Jurisdiction scope
    - Temporal relevance
    """
    
    def __init__(
        self,
        d_input: int = 1024,        # Input embedding dimension (SBERT/OpenAI)
        d_hidden: int = 512,        # Hidden layer dimension
        n_experts: int = 8,         # Number of legal experts
        dropout: float = 0.1,
        abstraction_levels: int = 4  # norm/principle/case/policy
    ):
        super().__init__()
        
        self.n_experts = n_experts
        self.abstraction_levels = abstraction_levels
        
        # Main routing network
        self.encoder = nn.Sequential(
            nn.Linear(d_input, d_hidden),
            nn.LayerNorm(d_hidden),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_hidden, d_hidden),
            nn.LayerNorm(d_hidden),
            nn.ReLU(),
            nn.Dropout(dropout)
        )
        
        # Expert routing head
        self.expert_head = nn.Linear(d_hidden, n_experts)
        
        # Auxiliary heads for better routing
        self.abstraction_head = nn.Linear(d_hidden, abstraction_levels)
        self.urgency_head = nn.Linear(d_hidden, 3)  # low/medium/high
        
        # Expert metadata (learned embeddings)
        self.expert_embeddings = nn.Parameter(torch.randn(n_experts, d_hidden // 2))
        self.domain_bias = nn.Parameter(torch.zeros(n_experts))
        
        self._init_weights()
    
    def _init_weights(self):
        """Initialize weights with legal domain priors"""
        for module in self.modules():
            if isinstance(module, nn.Linear):
                torch.nn.init.xavier_uniform_(module.weight)
                if module.bias is not None:
                    torch.nn.init.zeros_(module.bias)
    
    def forward(
        self, 
        query_embedding: torch.Tensor,
        context_features: Optional[torch.Tensor] = None,
        jurisdiction_mask: Optional[torch.Tensor] = None
    ) -> Dict[str, torch.Tensor]:
        """
        Forward pass for legal query routing.
        
        Args:
            query_embedding: [batch_size, d_input] - SBERT/OpenAI embeddings
            context_features: [batch_size, d_context] - Optional context (urgency, domain hints)
            jurisdiction_mask: [batch_size, n_experts] - Binary mask for jurisdiction filtering
            
        Returns:
            Dict with expert probabilities and auxiliary predictions
        """
        batch_size = query_embedding.size(0)
        
        # Encode query
        hidden = self.encoder(query_embedding)  # [batch_size, d_hidden]
        
        # Expert routing logits
        expert_logits = self.expert_head(hidden)  # [batch_size, n_experts]
        
        # Add domain bias (learned preferences per expert)
        expert_logits = expert_logits + self.domain_bias.unsqueeze(0)
        
        # Apply jurisdiction mask if provided
        if jurisdiction_mask is not None:
            expert_logits = expert_logits.masked_fill(~jurisdiction_mask.bool(), -1e9)
        
        # Auxiliary predictions
        abstraction_logits = self.abstraction_head(hidden)
        urgency_logits = self.urgency_head(hidden)
        
        return {
            'expert_logits': expert_logits,
            'expert_probs': F.softmax(expert_logits, dim=-1),
            'abstraction_logits': abstraction_logits,
            'abstraction_probs': F.softmax(abstraction_logits, dim=-1),
            'urgency_logits': urgency_logits,
            'urgency_probs': F.softmax(urgency_logits, dim=-1),
            'hidden_repr': hidden
        }


class RouterInference:
    """
    Inference utilities for Paris-SCM router.
    Implements Top-1, Top-2, and Full ensemble strategies.
    """
    
    def __init__(self, model: LegalRouterMini):
        self.model = model
        self.expert_names = [
            'experto_27401',
            'experto_contratacion_publica', 
            'experto_laboral',
            'experto_penal_economico',
            'experto_administrativo',
            'experto_datos_ai',
            'experto_etica_publica',
            'experto_psicologia_legal'
        ]
    
    def route_topk(
        self,
        query_embedding: torch.Tensor,
        strategy: str = 'top-2',
        jurisdiction_filter: Optional[List[str]] = None,
        confidence_threshold: float = 0.1
    ) -> Tuple[List[Tuple[int, float]], Dict]:
        """
        Route query to top-k experts based on strategy.
        
        Args:
            query_embedding: Query embedding tensor
            strategy: 'top-1', 'top-2', or 'full'
            jurisdiction_filter: List of allowed jurisdictions ['AR', 'EU', etc.]
            confidence_threshold: Minimum confidence for expert selection
            
        Returns:
            List of (expert_idx, weight) tuples and metadata
        """
        with torch.no_grad():
            # Create jurisdiction mask if needed
            jurisdiction_mask = None
            if jurisdiction_filter:
                jurisdiction_mask = self._create_jurisdiction_mask(jurisdiction_filter)
            
            # Forward pass
            outputs = self.model(query_embedding, jurisdiction_mask=jurisdiction_mask)
            probs = outputs['expert_probs'].squeeze()
            
            # Apply strategy
            if strategy == 'top-1':
                top_idx = torch.argmax(probs)
                selected_experts = [(top_idx.item(), 1.0)]
                
            elif strategy == 'top-2':
                top2_values, top2_indices = torch.topk(probs, k=2)
                # Renormalize weights
                weights = top2_values / top2_values.sum()
                selected_experts = [
                    (top2_indices[0].item(), weights[0].item()),
                    (top2_indices[1].item(), weights[1].item())
                ]
                
            elif strategy == 'full':
                # Filter by confidence threshold
                valid_experts = torch.where(probs > confidence_threshold)[0]
                valid_probs = probs[valid_experts]
                # Renormalize
                valid_probs = valid_probs / valid_probs.sum()
                selected_experts = [
                    (idx.item(), prob.item()) 
                    for idx, prob in zip(valid_experts, valid_probs)
                ]
                
            else:
                raise ValueError(f"Unknown strategy: {strategy}")
            
            # Metadata
            metadata = {
                'strategy': strategy,
                'abstraction_level': self._decode_abstraction(outputs['abstraction_probs']),
                'urgency_level': self._decode_urgency(outputs['urgency_probs']),
                'expert_probs': probs.cpu().numpy(),
                'confidence_scores': [prob for _, prob in selected_experts],
                'total_experts_considered': len(selected_experts)
            }
            
            return selected_experts, metadata
    
    def _create_jurisdiction_mask(self, allowed_jurisdictions: List[str]) -> torch.Tensor:
        """Create binary mask for jurisdiction filtering"""
        # Expert -> Jurisdiction mapping (configurable)
        expert_jurisdictions = {
            0: ['AR'],                    # Ley 27.401 (Argentina specific)
            1: ['AR'],                    # Contratación Pública (Argentina)
            2: ['AR', 'MERCOSUR'],        # Laboral (Argentina + regional)
            3: ['AR', 'LATAM'],           # Penal Económico (broader LATAM)
            4: ['AR', 'MERCOSUR'],        # Administrativo (regional)
            5: ['EU', 'AR'],              # Datos/AI (EU regs + local)
            6: ['GLOBAL', 'OCDE'],        # Ética Pública (international)
            7: ['GLOBAL']                 # Psicología Legal (universal)
        }
        
        mask = torch.zeros(self.model.n_experts, dtype=torch.bool)
        for expert_idx, expert_jurisdictions_list in expert_jurisdictions.items():
            if any(j in allowed_jurisdictions for j in expert_jurisdictions_list):
                mask[expert_idx] = True
                
        return mask.unsqueeze(0)  # Add batch dimension
    
    def _decode_abstraction(self, abstraction_probs: torch.Tensor) -> str:
        """Decode abstraction level from probabilities"""
        levels = ['norm', 'principle', 'case', 'policy']
        idx = torch.argmax(abstraction_probs).item()
        return levels[idx]
    
    def _decode_urgency(self, urgency_probs: torch.Tensor) -> str:
        """Decode urgency level from probabilities"""
        levels = ['low', 'medium', 'high']
        idx = torch.argmax(urgency_probs).item()
        return levels[idx]


def create_legal_router(config: Dict) -> Tuple[LegalRouterMini, RouterInference]:
    """
    Factory function to create legal router with configuration.
    
    Args:
        config: Dictionary with model configuration
        
    Returns:
        Tuple of (model, inference_engine)
    """
    model = LegalRouterMini(
        d_input=config.get('d_input', 1024),
        d_hidden=config.get('d_hidden', 512),
        n_experts=config.get('n_experts', 8),
        dropout=config.get('dropout', 0.1)
    )
    
    inference_engine = RouterInference(model)
    
    return model, inference_engine


# Training utilities
class RouterTrainingLoss(nn.Module):
    """Multi-task loss for router training"""
    
    def __init__(self, abstraction_weight: float = 0.1, urgency_weight: float = 0.05):
        super().__init__()
        self.abstraction_weight = abstraction_weight
        self.urgency_weight = urgency_weight
        self.expert_criterion = nn.CrossEntropyLoss()
        self.abstraction_criterion = nn.CrossEntropyLoss()
        self.urgency_criterion = nn.CrossEntropyLoss()
    
    def forward(self, outputs: Dict, targets: Dict) -> Dict:
        """
        Compute multi-task training loss.
        
        Args:
            outputs: Router model outputs
            targets: Ground truth labels
            
        Returns:
            Dict with loss components
        """
        # Main expert routing loss
        expert_loss = self.expert_criterion(
            outputs['expert_logits'], 
            targets['expert_labels']
        )
        
        # Auxiliary losses (if labels available)
        abstraction_loss = 0.0
        urgency_loss = 0.0
        
        if 'abstraction_labels' in targets:
            abstraction_loss = self.abstraction_criterion(
                outputs['abstraction_logits'],
                targets['abstraction_labels']
            )
            
        if 'urgency_labels' in targets:
            urgency_loss = self.urgency_criterion(
                outputs['urgency_logits'],
                targets['urgency_labels']
            )
        
        # Combined loss
        total_loss = (expert_loss + 
                     self.abstraction_weight * abstraction_loss +
                     self.urgency_weight * urgency_loss)
        
        return {
            'total_loss': total_loss,
            'expert_loss': expert_loss,
            'abstraction_loss': abstraction_loss,
            'urgency_loss': urgency_loss
        }