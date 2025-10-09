"""
Base schemas for Paris-SCM legal experts.
Standardized output format for legal responses with citations and gap analysis.
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any, Literal
from datetime import datetime
from enum import Enum


class JurisdictionEnum(str, Enum):
    """Supported jurisdictions"""
    AR = "AR"           # Argentina
    BR = "BR"           # Brazil  
    MX = "MX"           # Mexico
    EU = "EU"           # European Union
    MERCOSUR = "MERCOSUR"  # Mercosur region
    LATAM = "LATAM"     # Latin America
    GLOBAL = "GLOBAL"   # International/Universal
    OCDE = "OCDE"       # OECD standards


class DocumentTypeEnum(str, Enum):
    """Legal document types"""
    LEY = "ley"                    # Statute/Law
    DECRETO = "decreto"            # Decree
    RESOLUCION = "resolucion"      # Resolution
    DOCTRINA = "doctrina"          # Legal doctrine
    JURISPRUDENCIA = "jurisprudencia"  # Case law
    GUIA = "guia"                  # Guidance/Guidelines
    TRATADO = "tratado"            # Treaty
    CONSTITUCION = "constitucion"   # Constitution


class AbstractionLevelEnum(str, Enum):
    """Legal abstraction levels"""
    NORM = "norm"           # Specific legal rule
    PRINCIPLE = "principle"  # Legal principle
    CASE = "case"           # Specific case/situation
    POLICY = "policy"       # Policy/guidance


class RiskFlagEnum(str, Enum):
    """Legal risk flags"""
    JURISDICTION_AMBIGUITY = "jurisdiction_ambiguity"
    TEMPORAL_UNCERTAINTY = "temporal_uncertainty"
    ENFORCEMENT_GAP = "enforcement_gap"
    CONFLICTING_NORMS = "conflicting_norms"
    INSUFFICIENT_DATA = "insufficient_data"
    CROSS_BORDER_COMPLEXITY = "cross_border_complexity"
    REGULATORY_CHANGE_PENDING = "regulatory_change_pending"


class Citation(BaseModel):
    """Legal citation with verification metadata"""
    
    type: DocumentTypeEnum = Field(..., description="Type of legal document")
    title: str = Field(..., min_length=5, description="Document title")
    jurisdiction: JurisdictionEnum = Field(..., description="Legal jurisdiction")
    section: Optional[str] = Field(None, description="Specific section (Art. 9, § 2.1, etc.)")
    year: Optional[int] = Field(None, ge=1800, le=2030, description="Publication year")
    snippet: Optional[str] = Field(None, max_length=500, description="Relevant text excerpt")
    locator: str = Field(..., description="Unique document identifier")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    url: Optional[str] = Field(None, description="Official URL if available")
    verified: bool = Field(False, description="Citation verified against canonical source")
    
    @validator('section')
    def validate_section(cls, v):
        if v and len(v.strip()) == 0:
            return None
        return v


class EnforcementGap(BaseModel):
    """Documentation of formal law vs. enforcement reality gap"""
    
    formal_requirement: str = Field(..., description="What formal law requires")
    documented_reality: str = Field(..., description="What actually happens in practice")
    gap_percentage: Optional[float] = Field(None, ge=0.0, le=100.0, description="Gap magnitude (%)")
    gap_mechanisms: List[str] = Field(default_factory=list, description="Factors causing the gap")
    data_source: Optional[str] = Field(None, description="Source of enforcement data")
    confidence_level: Literal["low", "medium", "high"] = Field("medium", description="Data confidence")
    
    @validator('gap_mechanisms')
    def validate_mechanisms(cls, v):
        valid_mechanisms = [
            "administrative_burden", "enforcement_capacity", "economic_incentives",
            "social_norms", "corruption", "resource_constraints", "political_influence",
            "technical_complexity", "geographic_barriers", "cultural_factors"
        ]
        for mechanism in v:
            if mechanism not in valid_mechanisms:
                raise ValueError(f"Invalid gap mechanism: {mechanism}")
        return v


class Answer(BaseModel):
    """Legal analysis and conclusion"""
    
    summary: str = Field(..., min_length=20, max_length=1000, description="Concise actionable conclusion")
    reasoning: str = Field(..., min_length=50, max_length=2000, description="Step-by-step legal analysis")
    risk_flags: List[RiskFlagEnum] = Field(default_factory=list, description="Identified legal risks")
    abstraction_level: AbstractionLevelEnum = Field(..., description="Level of legal analysis")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Overall confidence in answer")
    
    @validator('summary')
    def validate_summary(cls, v):
        # Ensure summary is actionable (contains key action words)
        action_words = ["debe", "requiere", "prohibe", "permite", "establece", "exige", 
                       "must", "requires", "prohibits", "allows", "establishes"]
        if not any(word in v.lower() for word in action_words):
            raise ValueError("Summary must be actionable (contain action verbs)")
        return v


class RouterMetadata(BaseModel):
    """Router decision metadata"""
    
    strategy: Literal["top-1", "top-2", "full"] = Field(..., description="Routing strategy used")
    experts: List[Dict[str, float]] = Field(..., description="Expert weights used")
    abstraction_detected: AbstractionLevelEnum = Field(..., description="Detected query abstraction level")
    urgency_detected: Literal["low", "medium", "high"] = Field(..., description="Detected query urgency")
    jurisdiction_scope: List[JurisdictionEnum] = Field(..., description="Applicable jurisdictions")


class ExpertOutput(BaseModel):
    """Complete output from Paris-SCM legal expert system"""
    
    answer: Answer = Field(..., description="Legal analysis and conclusion")
    citations: List[Citation] = Field(..., min_items=1, description="Supporting legal citations")
    enforcement_gap: Optional[EnforcementGap] = Field(None, description="Formal vs. reality gap analysis")
    router: RouterMetadata = Field(..., description="Router decision metadata")
    
    # System metadata
    query_id: Optional[str] = Field(None, description="Unique query identifier")
    timestamp: datetime = Field(default_factory=datetime.now, description="Response timestamp")
    expert_version: str = Field("paris-scm-0.1.0", description="Expert system version")
    processing_time_ms: Optional[int] = Field(None, description="Processing time in milliseconds")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class QueryInput(BaseModel):
    """Standardized input for legal queries"""
    
    query_text: str = Field(..., min_length=10, max_length=2000, description="Legal question or scenario")
    jurisdiction_preference: Optional[List[JurisdictionEnum]] = Field(None, description="Preferred jurisdictions")
    urgency_level: Optional[Literal["low", "medium", "high"]] = Field(None, description="Query urgency")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")
    require_citations: bool = Field(True, description="Whether citations are required")
    include_gap_analysis: bool = Field(True, description="Whether to include enforcement gap analysis")
    
    @validator('query_text')
    def validate_query_text(cls, v):
        # Basic validation for legal queries
        if len(v.strip()) < 10:
            raise ValueError("Query too short for meaningful legal analysis")
        
        # Check for at least some legal content
        legal_indicators = [
            "ley", "derecho", "legal", "norma", "artículo", "decreto", "resolución",
            "law", "legal", "regulation", "article", "section", "compliance",
            "cumplimiento", "sanción", "multa", "procedimiento", "obligación"
        ]
        
        if not any(indicator in v.lower() for indicator in legal_indicators):
            raise ValueError("Query should contain legal terminology")
            
        return v.strip()


# Expert validation schemas
class ExpertValidationResult(BaseModel):
    """Results from expert output validation"""
    
    is_valid: bool = Field(..., description="Overall validation result")
    citation_accuracy: float = Field(..., ge=0.0, le=1.0, description="Citation accuracy score")
    reasoning_coherence: float = Field(..., ge=0.0, le=1.0, description="Logical coherence score")  
    jurisdiction_compliance: bool = Field(..., description="Jurisdiction scope compliance")
    errors: List[str] = Field(default_factory=list, description="Validation errors found")
    warnings: List[str] = Field(default_factory=list, description="Validation warnings")
    
    @validator('errors')
    def validate_errors(cls, v):
        if len(v) > 10:  # Too many errors indicate systemic issues
            raise ValueError("Too many validation errors - expert may need retraining")
        return v


# Training data schemas  
class ExpertTrainingExample(BaseModel):
    """Training example for expert fine-tuning"""
    
    query: str = Field(..., description="Input legal query")
    expert_target: str = Field(..., description="Target expert name")
    expected_citations: List[str] = Field(..., description="Expected citation locators")
    abstraction_level: AbstractionLevelEnum = Field(..., description="Query abstraction level")
    jurisdiction: JurisdictionEnum = Field(..., description="Primary jurisdiction")
    difficulty: Literal["easy", "medium", "hard"] = Field("medium", description="Query difficulty")


# Configuration schemas
class ExpertConfig(BaseModel):
    """Configuration for individual expert"""
    
    name: str = Field(..., description="Expert identifier")
    domain: str = Field(..., description="Legal domain specialty")
    jurisdictions: List[JurisdictionEnum] = Field(..., description="Covered jurisdictions")
    corpus_path: str = Field(..., description="Path to expert's corpus")
    index_path: str = Field(..., description="Path to FAISS index")
    model_path: Optional[str] = Field(None, description="Path to fine-tuned model")
    max_retrieval_docs: int = Field(6, ge=1, le=20, description="Max documents to retrieve")
    citation_threshold: float = Field(0.7, ge=0.0, le=1.0, description="Minimum citation confidence")


class SystemConfig(BaseModel):
    """Paris-SCM system configuration"""
    
    router_model_path: str = Field(..., description="Path to router model")
    experts: List[ExpertConfig] = Field(..., min_items=1, description="Expert configurations")
    default_strategy: Literal["top-1", "top-2", "full"] = Field("top-2", description="Default routing strategy")
    embedding_model: str = Field("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", description="Embedding model")
    max_response_time_ms: int = Field(5000, description="Maximum response time")
    enable_gap_detection: bool = Field(True, description="Enable enforcement gap detection")
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field("INFO", description="Logging level")