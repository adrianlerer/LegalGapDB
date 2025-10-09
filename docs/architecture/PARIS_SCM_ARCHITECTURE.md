# 🧠 Paris-SCM Architecture: Decentralized Legal AI for Non-WEIRD Jurisdictions

## Overview

Paris-SCM (Small Concept Models) applies the decentralized training paradigm from [Paris: A Decentralized Trained Open-Weight Diffusion Model](https://arxiv.org/abs/2510.03434) to legal concept modeling, specifically addressing post-colonial compliance dynamics that token-based Legal AI systematically fails to capture.

## Theoretical Foundation

### WEIRD Bias Problem
- **88%** of humanity lives in non-WEIRD (Western, Educated, Industrialized, Rich, Democratic) contexts
- Current Legal AI trained on formal texts from WEIRD jurisdictions (12% of humanity)
- **Enforcement Gap**: Systematic difference between written law and actual practice
- Token-based models cannot model the cultural-institutional context that determines compliance behavior

### Concept-Based vs Token-Based Models

#### Token-Based Limitations
```
Formal Law Text → Token Embedding → Prediction
"Registration required within 5 days" → [0.1, 0.8, ...] → "100% compliance expected"
```

#### Concept-Based Advantages  
```
Legal Concept Space → Cultural Context → Institutional History → Compliance Reality
"Registration Requirement" + "Post-Colonial Administrative Capacity" + "Informal Economy" → "42% actual compliance"
```

## Architecture Design

### Core Principle: Decentralized Expert Training

Following Paris methodology:
- **8 Independent Experts** trained without gradient/parameter synchronization  
- **Router Network** coordinates experts during inference
- **14× data efficiency** and **16× computational savings** vs monolithic models
- **Maintains quality** with minimal performance degradation

### Legal Domain Mapping

| Paris Component | SCM-Legal Component | Purpose |
|-----------------|---------------------|---------|
| Image Experts (8) | Legal Domain Experts (8) | Specialized knowledge |
| DINOv2 Clustering | SBERT Legal Clustering | Semantic partitioning |
| Noise-Aware Router | Abstraction-Level Router | Context recognition |  
| FID Metrics | Legal Precision Metrics | Quality validation |

## Expert Specialization

### Expert Domains (K=8)
1. **Ley 27.401/Compliance** - Corporate integrity programs
2. **Contratación Pública** - Public procurement law
3. **Derecho Laboral** - Labor law & informal employment
4. **Penal Económico** - Economic crime enforcement
5. **Administrativo Sancionador** - Administrative sanctions
6. **Protección de Datos/EU AI Act** - Data protection & AI governance
7. **Ética Pública/OCDE** - Public ethics & international standards
8. **Psicología Evolutiva Legal** - Behavioral compliance patterns

### Training Isolation Protocol
```python
# Each expert trains independently
for expert_k in range(8):
    corpus_k = semantic_clusters[k]  # Disjoint legal corpus
    expert_k.train(corpus_k)         # No parameter sharing
    # Zero synchronization between experts
```

## Router Architecture

### Input Processing
```python
def route_legal_query(query_text, context_level):
    embeddings = legal_embed(query_text)           # SBERT legal embeddings
    abstraction = detect_level(query_text)         # norm/principle/case/policy
    logits = router.forward(embeddings, abstraction)
    expert_probs = softmax(logits)                 # p(k|query, context)
    return select_strategy(expert_probs)           # Top-1/Top-2/Full
```

### Inference Strategies
- **Top-1**: Single expert (efficiency focus)
- **Top-2**: Two experts weighted (quality focus)  
- **Full Ensemble**: All 8 experts (research/validation only)

## Data Architecture

### Legal Corpus Partitioning
```
Total Corpus → SBERT Embeddings → K-Means(k=8) → Expert Clusters
├── Cluster 0: Ley 27.401 + compliance doctrine
├── Cluster 1: Public procurement + administrative law  
├── Cluster 2: Labor law + informality studies
├── ...
└── Cluster 7: Behavioral legal psychology
```

### Index Structure (per Expert)
```
experts/experto_27401/
├── index/
│   ├── faiss.index          # FAISS vector index
│   ├── vectors.npy          # Embedding matrix
│   └── meta.jsonl           # Document metadata
├── retriever.py             # RAG search logic
└── answerer.py              # Response generation
```

## Quality Metrics (Legal-Specific)

Replacing computer vision FID with legal precision metrics:

| Metric | Definition | Target |
|--------|------------|--------|
| **Citation Precision** | % citations with correct article/section | >90% |
| **NLI Coherence** | Logical consistency between reasoning steps | >85% |
| **Groundedness** | % statements with legal source backing | >95% |
| **Jurisdiction Accuracy** | Correct legal system identification | >98% |
| **Enforcement Reality** | Gaps between formal law and practice | Documented |

## Output Schema

### Standardized Legal Response
```json
{
  "answer": {
    "summary": "Actionable legal conclusion",
    "reasoning": "Step-by-step legal analysis", 
    "risk_flags": ["jurisdiction_ambiguity", "enforcement_gap"]
  },
  "citations": [{
    "type": "ley|decreto|doctrina|jurisprudencia",
    "title": "Ley 27.401",
    "jurisdiction": "AR", 
    "section": "Art. 9",
    "year": 2018,
    "snippet": "Relevant text passage...",
    "confidence": 0.94
  }],
  "router": {
    "strategy": "Top-2",
    "experts": [
      {"name": "experto_27401", "weight": 0.67},
      {"name": "experto_contratacion_publica", "weight": 0.33}
    ]
  },
  "enforcement_gap": {
    "formal_requirement": "100% compliance expected",
    "documented_reality": "31% actual compliance (INDEC 2024)",
    "gap_mechanisms": ["administrative_burden", "enforcement_capacity"]
  }
}
```

## Integration with LegalGapDB

### Bidirectional Enhancement
1. **Paris-SCM → LegalGapDB**: Automated gap detection through expert ensemble disagreement
2. **LegalGapDB → Paris-SCM**: Training data for enforcement reality modeling
3. **Continuous Learning**: Real-world compliance data improves expert accuracy

### Gap Detection Pipeline
```python
def detect_enforcement_gap(legal_concept):
    formal_expert = router.route(legal_concept, level="formal_law")
    reality_expert = router.route(legal_concept, level="enforcement_data")
    
    gap_magnitude = measure_divergence(formal_expert.output, reality_expert.output)
    if gap_magnitude > threshold:
        return create_legalgap_case(formal_expert, reality_expert, gap_magnitude)
```

## Deployment Strategy

### Production Configuration
- **Default**: Top-1 routing (sub-200ms latency)
- **Critical Queries**: Top-2 routing (legal opinions, sanctions)
- **Research Mode**: Full ensemble (gap analysis, validation)

### Privacy & Compartmentalization  
- Each expert accesses only its domain corpus
- No cross-expert information leakage
- Audit trail preserves expert attribution

## Performance Benchmarks

Based on Paris results, projected for legal domain:

| Metric | Monolithic Model | Paris-SCM | Improvement |
|--------|------------------|-----------|-------------|
| Training Data | 100% corpus | 7% per expert | 14× efficiency |
| Compute Cost | 100% | 6.25% per expert | 16× savings |
| Inference Latency | 1.0× | 0.8× (Top-1) | 25% faster |
| Legal Precision | Baseline | +12% (Top-2) | Quality gain |

## Implementation Roadmap

### Phase 1: MVP (Current)
- [ ] 3 Core experts (27.401, Procurement, Labor)
- [ ] Basic router with Top-2 strategy  
- [ ] Legal citation validation
- [ ] JSON output schema

### Phase 2: Full Deployment
- [ ] 8 Complete expert domains
- [ ] Advanced gap detection
- [ ] Real-time LegalGapDB integration
- [ ] Production API endpoints

### Phase 3: Research Extensions
- [ ] Cross-jurisdiction expert training
- [ ] Temporal gap evolution modeling
- [ ] Behavioral prediction validation

## References

1. **Paris Framework**: Jiang, Z. et al. (2025). "Paris: A Decentralized Trained Open-Weight Diffusion Model." arXiv:2510.03434
2. **WEIRD Theory**: Henrich, J. (2020). "The WEIRDest People in the World: How the West Became Psychologically Peculiar"
3. **Legal Gaps**: Lerer, I.A. (2025). "Beyond WEIRD Legal AI: Why Token-Based Legal AI Cannot Model Post-Colonial Compliance Dynamics"
4. **Enforcement Data**: LegalGapDB Cases AR-LAB-001 through AR-FAM-001

---

*Architecture designed for 88% of humanity living in non-WEIRD legal contexts*