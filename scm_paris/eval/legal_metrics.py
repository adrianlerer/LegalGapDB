"""
Legal-specific quality metrics for Paris-SCM evaluation.
Replaces computer vision FID with legal domain precision measures.
"""

import re
import json
import numpy as np
from typing import List, Dict, Tuple, Optional, Union
from dataclasses import dataclass
from pathlib import Path

import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


@dataclass
class LegalMetricsResult:
    """Results from legal quality evaluation"""
    
    citation_precision: float
    nli_coherence: float  
    groundedness: float
    jurisdiction_accuracy: float
    gap_detection_rate: float
    overall_score: float
    
    # Detailed breakdowns
    citation_errors: List[str]
    coherence_violations: List[str]
    ungrounded_statements: List[str]
    jurisdiction_mismatches: List[str]
    
    def to_dict(self) -> Dict:
        return {
            'scores': {
                'citation_precision': self.citation_precision,
                'nli_coherence': self.nli_coherence,
                'groundedness': self.groundedness, 
                'jurisdiction_accuracy': self.jurisdiction_accuracy,
                'gap_detection_rate': self.gap_detection_rate,
                'overall_score': self.overall_score
            },
            'errors': {
                'citation_errors': self.citation_errors,
                'coherence_violations': self.coherence_violations,
                'ungrounded_statements': self.ungrounded_statements,
                'jurisdiction_mismatches': self.jurisdiction_mismatches
            }
        }


class CitationValidator:
    """Validates legal citation accuracy and format compliance"""
    
    def __init__(self):
        # Legal citation patterns (Argentina focus, extensible)
        self.citation_patterns = {
            'ley': r'Ley\s+(\d+\.?\d*)',
            'articulo': r'Art(?:ículo|\.)?\s*(\d+(?:\s*bis)?(?:\s*ter)?)',
            'inciso': r'inc(?:iso|\.)?\s*([a-z]|\d+)',
            'decreto': r'Decreto\s+(\d+/\d+|\d+\.\d+)',
            'resolucion': r'Resolución\s+(\d+/\d+|\d+\.\d+)'
        }
        
        # Canonical legal sources for verification
        self.canonical_sources = self._load_canonical_sources()
    
    def _load_canonical_sources(self) -> Dict[str, Dict]:
        """Load canonical legal source database"""
        # In production: load from InfoLeg/Boletín Oficial API
        return {
            'AR_L27401': {
                'title': 'Ley 27.401 - Responsabilidad Penal Empresaria',
                'articles': list(range(1, 40)),  # Articles 1-39
                'year': 2017,
                'jurisdiction': 'AR'
            },
            'AR_LCT': {
                'title': 'Ley de Contrato de Trabajo',
                'articles': list(range(1, 278)),  # Articles 1-277
                'year': 1974,
                'jurisdiction': 'AR'
            }
        }
    
    def validate_citations(self, citations: List[Dict]) -> Tuple[float, List[str]]:
        """
        Validate citation accuracy against canonical sources.
        
        Args:
            citations: List of citation dictionaries
            
        Returns:
            Tuple of (precision_score, error_list)
        """
        if not citations:
            return 0.0, ["No citations provided"]
            
        errors = []
        correct_citations = 0
        
        for i, citation in enumerate(citations):
            citation_errors = self._validate_single_citation(citation)
            if citation_errors:
                errors.extend([f"Citation {i+1}: {err}" for err in citation_errors])
            else:
                correct_citations += 1
        
        precision = correct_citations / len(citations)
        return precision, errors
    
    def _validate_single_citation(self, citation: Dict) -> List[str]:
        """Validate individual citation"""
        errors = []
        
        # Required fields validation
        required_fields = ['type', 'title', 'jurisdiction', 'locator']
        for field in required_fields:
            if field not in citation or not citation[field]:
                errors.append(f"Missing required field: {field}")
        
        if errors:  # Skip further validation if basic fields missing
            return errors
            
        # Format validation
        citation_type = citation.get('type', '').lower()
        title = citation.get('title', '')
        section = citation.get('section', '')
        
        if citation_type == 'ley':
            # Validate law citation format
            if not re.search(self.citation_patterns['ley'], title):
                errors.append("Invalid law citation format")
                
            if section and not re.search(self.citation_patterns['articulo'], section):
                errors.append("Invalid article section format")
        
        # Canonical source verification
        locator = citation.get('locator', '')
        if locator in self.canonical_sources:
            source = self.canonical_sources[locator]
            
            # Verify jurisdiction
            if citation.get('jurisdiction') != source['jurisdiction']:
                errors.append(f"Jurisdiction mismatch: {citation.get('jurisdiction')} vs {source['jurisdiction']}")
            
            # Verify article exists (if specified)
            if section:
                article_match = re.search(r'(\d+)', section)
                if article_match:
                    article_num = int(article_match.group(1))
                    if article_num not in source['articles']:
                        errors.append(f"Article {article_num} does not exist in {source['title']}")
        
        return errors


class NLICoherenceEvaluator:
    """Evaluates logical coherence of legal reasoning using NLI"""
    
    def __init__(self, model_name: str = "microsoft/deberta-v3-base-mnli"):
        self.model = SentenceTransformer(model_name)
        self.threshold = 0.7  # Coherence threshold
    
    def evaluate_coherence(self, reasoning_text: str, citations: List[Dict]) -> Tuple[float, List[str]]:
        """
        Evaluate logical coherence between reasoning and citations.
        
        Args:
            reasoning_text: Legal reasoning text  
            citations: Supporting citations
            
        Returns:
            Tuple of (coherence_score, violations_list)
        """
        if not reasoning_text or not citations:
            return 0.0, ["Insufficient content for coherence evaluation"]
        
        # Split reasoning into logical steps
        reasoning_steps = self._extract_reasoning_steps(reasoning_text)
        citation_texts = [c.get('snippet', c.get('title', '')) for c in citations]
        
        violations = []
        coherence_scores = []
        
        for i, step in enumerate(reasoning_steps):
            # Check if reasoning step is supported by citations
            step_score = self._compute_support_score(step, citation_texts)
            coherence_scores.append(step_score)
            
            if step_score < self.threshold:
                violations.append(f"Step {i+1} lacks sufficient citation support: {step[:100]}...")
        
        # Check for logical contradictions within reasoning
        contradiction_score = self._detect_contradictions(reasoning_steps)
        if contradiction_score > 0.3:  # High contradiction threshold
            violations.append("Internal logical contradictions detected in reasoning")
            
        overall_coherence = np.mean(coherence_scores) * (1 - contradiction_score)
        return overall_coherence, violations
    
    def _extract_reasoning_steps(self, text: str) -> List[str]:
        """Extract logical steps from reasoning text"""
        # Split by common legal reasoning markers
        markers = [r'En primer lugar', r'Por otra parte', r'Asimismo', r'En consecuencia', 
                  r'Por lo tanto', r'Dado que', r'Considerando que']
        
        steps = [text]  # Start with full text
        for marker in markers:
            new_steps = []
            for step in steps:
                parts = re.split(marker, step, flags=re.IGNORECASE)
                new_steps.extend([p.strip() for p in parts if p.strip()])
            steps = new_steps
            
        # Filter out very short steps
        return [step for step in steps if len(step) > 20]
    
    def _compute_support_score(self, reasoning_step: str, citation_texts: List[str]) -> float:
        """Compute how well citations support a reasoning step"""
        if not citation_texts:
            return 0.0
            
        step_embedding = self.model.encode([reasoning_step])
        citation_embeddings = self.model.encode(citation_texts)
        
        # Compute semantic similarity
        similarities = F.cosine_similarity(
            torch.tensor(step_embedding),
            torch.tensor(citation_embeddings)
        )
        
        return float(torch.max(similarities))
    
    def _detect_contradictions(self, reasoning_steps: List[str]) -> float:
        """Detect logical contradictions within reasoning steps"""
        if len(reasoning_steps) < 2:
            return 0.0
            
        embeddings = self.model.encode(reasoning_steps)
        
        # Look for steps that are semantically opposite
        contradiction_signals = 0
        total_pairs = 0
        
        for i in range(len(reasoning_steps)):
            for j in range(i + 1, len(reasoning_steps)):
                similarity = F.cosine_similarity(
                    torch.tensor(embeddings[i:i+1]),
                    torch.tensor(embeddings[j:j+1])
                )
                
                # Very low similarity might indicate contradiction
                if similarity < -0.3:  # Negative similarity threshold
                    contradiction_signals += 1
                total_pairs += 1
        
        return contradiction_signals / total_pairs if total_pairs > 0 else 0.0


class GroundednessEvaluator:
    """Evaluates whether statements are grounded in legal sources"""
    
    def __init__(self):
        self.legal_statement_patterns = [
            r'(establece que|dispone que|requiere que|prohibe|permite)',
            r'(según el artículo|conforme al|de acuerdo con)',
            r'(la ley establece|el decreto dispone|la resolución indica)'
        ]
    
    def evaluate_groundedness(self, summary: str, citations: List[Dict]) -> Tuple[float, List[str]]:
        """
        Evaluate what percentage of statements are backed by legal sources.
        
        Args:
            summary: Legal summary text
            citations: Supporting citations
            
        Returns:
            Tuple of (groundedness_score, ungrounded_statements)
        """
        if not summary:
            return 0.0, ["No summary provided"]
            
        # Extract legal statements from summary
        statements = self._extract_legal_statements(summary)
        citation_snippets = [c.get('snippet', '') for c in citations if c.get('snippet')]
        
        ungrounded = []
        grounded_count = 0
        
        for statement in statements:
            if self._is_statement_grounded(statement, citation_snippets):
                grounded_count += 1
            else:
                ungrounded.append(statement)
        
        groundedness_score = grounded_count / len(statements) if statements else 0.0
        return groundedness_score, ungrounded
    
    def _extract_legal_statements(self, text: str) -> List[str]:
        """Extract individual legal statements from text"""
        # Split by sentence boundaries
        sentences = re.split(r'[.!?]', text)
        
        # Filter for legal statements (contain legal language)
        legal_statements = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 10:  # Too short to be meaningful
                continue
                
            # Check if contains legal language
            contains_legal_language = any(
                re.search(pattern, sentence, re.IGNORECASE)
                for pattern in self.legal_statement_patterns
            )
            
            if contains_legal_language:
                legal_statements.append(sentence)
        
        return legal_statements
    
    def _is_statement_grounded(self, statement: str, citation_snippets: List[str]) -> bool:
        """Check if a statement is supported by citation snippets"""
        if not citation_snippets:
            return False
            
        # Simple keyword overlap approach (can be enhanced with embeddings)
        statement_words = set(re.findall(r'\w+', statement.lower()))
        
        for snippet in citation_snippets:
            snippet_words = set(re.findall(r'\w+', snippet.lower()))
            
            # If significant word overlap, consider grounded
            overlap = len(statement_words & snippet_words)
            if overlap >= min(3, len(statement_words) // 2):
                return True
                
        return False


class GapDetectionEvaluator:
    """Evaluates enforcement gap detection accuracy"""
    
    def __init__(self, known_gaps_db: Optional[str] = None):
        # Load known enforcement gaps from LegalGapDB
        self.known_gaps = self._load_known_gaps(known_gaps_db)
    
    def _load_known_gaps(self, db_path: Optional[str]) -> Dict[str, Dict]:
        """Load known enforcement gaps for validation"""
        # In production: load from LegalGapDB cases
        return {
            'AR_LAB_REGISTRATION': {
                'formal': '100% registration required within 5 days',
                'reality': '42% actually registered (INDEC Q4 2024)',
                'gap_percentage': 58.0,
                'mechanisms': ['administrative_burden', 'enforcement_capacity']
            },
            'AR_CORP_INTEGRITY': {
                'formal': '100% integrity programs required (Ley 27.401)',
                'reality': '31% full implementation (OEADE 2025)',
                'gap_percentage': 69.0,
                'mechanisms': ['cost_barriers', 'lack_enforcement']
            }
        }
    
    def evaluate_gap_detection(
        self, 
        predicted_gaps: List[Dict], 
        query_context: str
    ) -> Tuple[float, List[str]]:
        """
        Evaluate accuracy of gap detection against known cases.
        
        Args:
            predicted_gaps: Model's gap predictions
            query_context: Original query for context matching
            
        Returns:
            Tuple of (detection_accuracy, missed_gaps)
        """
        # Find relevant known gaps for this query
        relevant_gaps = self._find_relevant_gaps(query_context)
        
        if not relevant_gaps:
            # No known gaps to validate against
            return 1.0, []
        
        detected_gaps = set()
        missed_gaps = []
        
        for gap_id, known_gap in relevant_gaps.items():
            gap_detected = self._check_gap_detected(known_gap, predicted_gaps)
            if gap_detected:
                detected_gaps.add(gap_id)
            else:
                missed_gaps.append(f"Missed gap: {gap_id}")
        
        detection_rate = len(detected_gaps) / len(relevant_gaps)
        return detection_rate, missed_gaps
    
    def _find_relevant_gaps(self, query_context: str) -> Dict[str, Dict]:
        """Find known gaps relevant to the query context"""
        relevant = {}
        
        # Simple keyword matching (can be enhanced with embeddings)
        query_lower = query_context.lower()
        
        for gap_id, gap_data in self.known_gaps.items():
            # Check if query relates to this gap domain
            if 'lab' in gap_id.lower() and any(word in query_lower for word in ['trabajo', 'labor', 'registro', 'empleado']):
                relevant[gap_id] = gap_data
            elif 'corp' in gap_id.lower() and any(word in query_lower for word in ['integridad', 'compliance', '27.401']):
                relevant[gap_id] = gap_data
                
        return relevant
    
    def _check_gap_detected(self, known_gap: Dict, predicted_gaps: List[Dict]) -> bool:
        """Check if a known gap was detected in predictions"""
        for predicted in predicted_gaps:
            # Check gap percentage similarity
            known_pct = known_gap.get('gap_percentage', 0)
            pred_pct = predicted.get('gap_percentage', 0)
            
            if abs(known_pct - pred_pct) < 15:  # Within 15 percentage points
                return True
                
            # Check mechanism overlap
            known_mechanisms = set(known_gap.get('mechanisms', []))
            pred_mechanisms = set(predicted.get('gap_mechanisms', []))
            
            if known_mechanisms & pred_mechanisms:  # At least one mechanism overlap
                return True
                
        return False


class LegalQualityEvaluator:
    """Main evaluator combining all legal quality metrics"""
    
    def __init__(self, config: Optional[Dict] = None):
        config = config or {}
        
        self.citation_validator = CitationValidator()
        self.nli_evaluator = NLICoherenceEvaluator()
        self.groundedness_evaluator = GroundednessEvaluator()
        self.gap_evaluator = GapDetectionEvaluator()
        
        # Metric weights for overall score
        self.weights = config.get('weights', {
            'citation_precision': 0.25,
            'nli_coherence': 0.20,
            'groundedness': 0.25,
            'jurisdiction_accuracy': 0.15,
            'gap_detection_rate': 0.15
        })
    
    def evaluate_response(self, response: Dict, query_context: str = "") -> LegalMetricsResult:
        """
        Comprehensive evaluation of legal response quality.
        
        Args:
            response: Legal response following ExpertOutput schema
            query_context: Original query for context
            
        Returns:
            LegalMetricsResult with all quality metrics
        """
        answer = response.get('answer', {})
        citations = response.get('citations', [])
        enforcement_gaps = response.get('enforcement_gap')
        
        # 1. Citation precision
        citation_precision, citation_errors = self.citation_validator.validate_citations(citations)
        
        # 2. NLI coherence
        reasoning = answer.get('reasoning', '')
        nli_coherence, coherence_violations = self.nli_evaluator.evaluate_coherence(reasoning, citations)
        
        # 3. Groundedness
        summary = answer.get('summary', '')
        groundedness, ungrounded_statements = self.groundedness_evaluator.evaluate_groundedness(summary, citations)
        
        # 4. Jurisdiction accuracy (simplified - checks citation jurisdictions)
        jurisdiction_accuracy = self._evaluate_jurisdiction_accuracy(response)
        jurisdiction_mismatches = []  # TODO: Implement detailed jurisdiction checking
        
        # 5. Gap detection rate
        predicted_gaps = [enforcement_gaps] if enforcement_gaps else []
        gap_detection_rate, missed_gaps = self.gap_evaluator.evaluate_gap_detection(predicted_gaps, query_context)
        
        # Calculate overall score
        overall_score = (
            self.weights['citation_precision'] * citation_precision +
            self.weights['nli_coherence'] * nli_coherence +
            self.weights['groundedness'] * groundedness +
            self.weights['jurisdiction_accuracy'] * jurisdiction_accuracy +
            self.weights['gap_detection_rate'] * gap_detection_rate
        )
        
        return LegalMetricsResult(
            citation_precision=citation_precision,
            nli_coherence=nli_coherence,
            groundedness=groundedness,
            jurisdiction_accuracy=jurisdiction_accuracy,
            gap_detection_rate=gap_detection_rate,
            overall_score=overall_score,
            citation_errors=citation_errors,
            coherence_violations=coherence_violations,
            ungrounded_statements=ungrounded_statements,
            jurisdiction_mismatches=jurisdiction_mismatches
        )
    
    def _evaluate_jurisdiction_accuracy(self, response: Dict) -> float:
        """Evaluate jurisdiction scope accuracy"""
        citations = response.get('citations', [])
        router_meta = response.get('router', {})
        
        if not citations:
            return 0.0
            
        # Check if all citations have consistent jurisdiction
        jurisdictions = [c.get('jurisdiction') for c in citations if c.get('jurisdiction')]
        
        if not jurisdictions:
            return 0.0
            
        # Simple consistency check - all citations should have valid jurisdictions
        valid_jurisdictions = ['AR', 'BR', 'MX', 'EU', 'MERCOSUR', 'LATAM', 'GLOBAL', 'OCDE']
        valid_count = sum(1 for j in jurisdictions if j in valid_jurisdictions)
        
        return valid_count / len(jurisdictions)


def run_batch_evaluation(responses: List[Dict], queries: List[str] = None) -> Dict:
    """
    Run batch evaluation on multiple legal responses.
    
    Args:
        responses: List of legal responses to evaluate
        queries: Optional list of corresponding queries
        
    Returns:
        Dict with aggregate statistics and per-response results
    """
    evaluator = LegalQualityEvaluator()
    results = []
    
    for i, response in enumerate(responses):
        query_context = queries[i] if queries and i < len(queries) else ""
        result = evaluator.evaluate_response(response, query_context)
        results.append(result)
    
    # Aggregate statistics
    scores = [r.overall_score for r in results]
    citation_scores = [r.citation_precision for r in results]
    coherence_scores = [r.nli_coherence for r in results]
    groundedness_scores = [r.groundedness for r in results]
    
    aggregate_stats = {
        'summary': {
            'total_responses': len(responses),
            'mean_overall_score': np.mean(scores),
            'std_overall_score': np.std(scores),
            'mean_citation_precision': np.mean(citation_scores),
            'mean_coherence': np.mean(coherence_scores),
            'mean_groundedness': np.mean(groundedness_scores)
        },
        'distribution': {
            'high_quality': sum(1 for s in scores if s >= 0.8),
            'medium_quality': sum(1 for s in scores if 0.6 <= s < 0.8),
            'low_quality': sum(1 for s in scores if s < 0.6)
        },
        'detailed_results': [r.to_dict() for r in results]
    }
    
    return aggregate_stats


if __name__ == "__main__":
    # Example usage
    sample_response = {
        'answer': {
            'summary': 'La Ley 27.401 establece que las empresas deben implementar programas de integridad.',
            'reasoning': 'Según el artículo 9 de la Ley 27.401, los programas deben incluir capacitación y canales de denuncia.',
            'risk_flags': ['enforcement_gap'],
            'confidence': 0.9
        },
        'citations': [{
            'type': 'ley',
            'title': 'Ley 27.401',
            'jurisdiction': 'AR',
            'section': 'Art. 9',
            'locator': 'AR_L27401_Art9',
            'confidence': 0.95,
            'snippet': 'Las personas jurídicas deberán adoptar un Programa de Integridad...'
        }],
        'enforcement_gap': {
            'formal_requirement': '100% implementation required',
            'documented_reality': '31% full implementation',
            'gap_percentage': 69.0,
            'gap_mechanisms': ['cost_barriers', 'lack_enforcement']
        }
    }
    
    evaluator = LegalQualityEvaluator()
    result = evaluator.evaluate_response(sample_response, "¿Qué requiere la Ley 27.401?")
    
    print("Legal Quality Evaluation Results:")
    print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))