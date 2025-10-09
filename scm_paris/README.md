# 🧠 Paris-SCM: Decentralized Legal AI for Non-WEIRD Jurisdictions

**Small Concept Models for Legal Enforcement Gap Analysis**

[![Paper](https://img.shields.io/badge/Paper-Beyond%20WEIRD%20Bias-blue.svg)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5576850)
[![Architecture](https://img.shields.io/badge/Architecture-Paris--Inspired-green.svg)](https://arxiv.org/abs/2510.03434)
[![Dataset](https://img.shields.io/badge/Dataset-LegalGapDB-orange.svg)](../README.md)

## 🎯 Mission

Paris-SCM adapts the decentralized training paradigm from [Paris: A Decentralized Trained Open-Weight Diffusion Model](https://arxiv.org/abs/2510.03434) to legal concept modeling, specifically addressing **post-colonial compliance dynamics** that token-based Legal AI systems systematically fail to model.

### The WEIRD Problem in Legal AI

- **88%** of humanity lives in non-WEIRD contexts where formal law diverges from enforcement reality
- Current Legal AI exhibits **WEIRD bias**: trained on formal texts from Western jurisdictions (12% of humanity)  
- **Token-based models** cannot capture the cultural-institutional context determining actual compliance behavior
- **Concept-based models** with enforcement gap awareness can model the reality experienced by the Global Majority

## 🏗️ Architecture Overview

### Core Innovation: Decentralized Legal Experts

```
Query → Router → Expert Selection → Legal Analysis → Gap-Aware Response
         ↓              ↓                ↓              ↓
    Abstraction    Independent      Formal Law +    Citations +
    Detection      Training         Reality Data    Enforcement
                  (No Sync)                        Gap Analysis
```

### Performance Benefits (Projected from Paris)
- **14× data efficiency**: Each expert trains on domain-specific corpus (7% of total)
- **16× computational savings**: Parallel expert training without synchronization  
- **Quality maintenance**: Top-2 routing maintains or improves accuracy vs monolithic models
- **Gap detection**: Identifies systematic differences between formal law and practice

## 📁 System Structure

```
scm_paris/
├── router_scm/              # Lightweight routing transformer
│   ├── model.py            # Router architecture & inference
│   ├── train.py            # Multi-task training pipeline
│   └── train_data.jsonl    # Router training examples
├── experts/                 # Independent legal experts  
│   ├── experto_27401/      # Corporate integrity (Ley 27.401)
│   ├── experto_contratacion_publica/  # Public procurement
│   ├── experto_laboral/    # Labor law & informality
│   └── base/
│       ├── schema.py       # Standardized output format
│       └── guardrails.py   # Legal validation utilities
├── eval/                   # Legal-specific metrics
├── data_prep/              # Corpus clustering & indexing
├── serving/                # API endpoints & response fusion
└── configs/                # Expert & system configuration
```

## 🎓 Expert Specialization

### Legal Domain Experts (8 Independent Models)

| Expert | Domain | Jurisdiction | Training Corpus | Gap Focus |
|--------|--------|--------------|-----------------|-----------|
| **experto_27401** | Corporate Integrity | AR | Ley 27.401 + compliance | Implementation gaps |
| **experto_contratacion_publica** | Public Procurement | AR | Procurement law + OA | Bidding irregularities |  
| **experto_laboral** | Labor Law | AR + MERCOSUR | LCT + informality data | Registration gaps (42%) |
| **experto_penal_economico** | Economic Crime | AR + LATAM | Penal + enforcement | Conviction gaps |
| **experto_administrativo** | Administrative Law | AR + MERCOSUR | Administrative sanctions | Enforcement capacity |
| **experto_datos_ai** | Data Protection | EU + AR | GDPR + Local laws | Cross-border compliance |
| **experto_etica_publica** | Public Ethics | GLOBAL + OCDE | International standards | Cultural adaptation |
| **experto_psicologia_legal** | Legal Psychology | GLOBAL | Henrich + behavioral | Compliance psychology |

### Training Protocol: Zero Synchronization
```python
# Each expert trains independently on its corpus cluster
for expert_k in legal_experts:
    corpus_k = semantic_partition[k]      # Disjoint legal texts
    expert_k.train(corpus_k, isolation=True)  # No gradient sharing
    expert_k.build_rag_index(corpus_k)   # Independent RAG system
    # Zero communication between experts during training
```

## 🧮 Router Intelligence

### Multi-Task Legal Routing
```python
class LegalRouterMini(nn.Module):
    """
    Lightweight transformer for expert selection:
    - Expert probabilities p(k|query, context)  
    - Abstraction level (norm/principle/case/policy)
    - Urgency detection (low/medium/high)
    - Jurisdiction scope identification
    """
```

### Inference Strategies
- **Top-1**: Fastest (single expert, <200ms)
- **Top-2**: Balanced (quality + speed, recommended)  
- **Full**: Research (all 8 experts, gap analysis focus)

## 📊 Output Schema: Gap-Aware Legal Responses

### Standardized Legal Analysis
```json
{
  "answer": {
    "summary": "Actionable legal conclusion",
    "reasoning": "Step-by-step analysis citing specific articles",
    "risk_flags": ["enforcement_gap", "jurisdiction_ambiguity"],
    "confidence": 0.92
  },
  "citations": [{
    "type": "ley",
    "title": "Ley 27.401", 
    "section": "Art. 9",
    "jurisdiction": "AR",
    "confidence": 0.94,
    "verified": true
  }],
  "enforcement_gap": {
    "formal_requirement": "100% integrity program implementation required",
    "documented_reality": "31% full implementation (OEADE 2025)",
    "gap_mechanisms": ["enforcement_capacity", "cost_barriers"],
    "data_source": "LegalGapDB Case AR-CORP-001"
  },
  "router": {
    "strategy": "top-2",
    "experts": [
      {"name": "experto_27401", "weight": 0.67},
      {"name": "experto_contratacion_publica", "weight": 0.33}
    ]
  }
}
```

## 🔬 Legal-Specific Quality Metrics

Replacing computer vision metrics with legal precision measures:

| Metric | Definition | Target | Implementation |
|--------|------------|--------|----------------|
| **Citation Precision** | % citations with correct article/section | >90% | Regex + canonical source validation |
| **NLI Coherence** | Logical consistency in reasoning | >85% | Legal NLI model scoring |
| **Groundedness** | % statements backed by legal sources | >95% | Attribution scoring |
| **Jurisdiction Accuracy** | Correct legal system identification | >98% | Multi-label classification |
| **Gap Detection Rate** | % of known gaps correctly identified | >80% | Validation against LegalGapDB |

## 🚀 Quick Start

### 1. Router Training
```bash
cd router_scm/
python train.py --data train_data.jsonl --epochs 50 --batch_size 32
```

### 2. Expert Index Building  
```bash
cd data_prep/
python build_index.py --expert experto_27401 --corpus ../experts/experto_27401/meta.jsonl
```

### 3. Legal Query Processing
```python
from serving.api import ParisLegalAPI

api = ParisLegalAPI()
response = api.query(
    "¿Qué elementos debe incluir un programa de integridad según la Ley 27.401?",
    strategy="top-2",
    jurisdiction=["AR"],
    include_gap_analysis=True
)
print(response.json())
```

## 📈 Benchmark Results (Projected)

Based on Paris architecture applied to legal domain:

| Model Type | Training Data | Compute Cost | Legal Precision | Gap Detection |
|------------|---------------|--------------|-----------------|---------------|
| **Monolithic Legal LLM** | 100% corpus | 100% | Baseline | Limited |
| **Paris-SCM (Top-1)** | 7% per expert | 6.25% | +8% | Enhanced |
| **Paris-SCM (Top-2)** | 7% per expert | 12.5% | +15% | High accuracy |

## 🔗 Integration with LegalGapDB

### Bidirectional Enhancement
1. **Paris-SCM → LegalGapDB**: Automated gap detection through expert disagreement
2. **LegalGapDB → Paris-SCM**: Real-world compliance data for training
3. **Continuous Learning**: Gap cases improve expert accuracy over time

### Gap Detection Pipeline
```python
def detect_new_gaps(legal_query):
    formal_response = route_to_expert(query, level="formal_law")  
    reality_response = route_to_expert(query, level="enforcement_data")
    
    if divergence(formal_response, reality_response) > threshold:
        return create_legalgap_case(formal_response, reality_response)
```

## 📚 Research Foundation

### Core Papers
1. **Henrich, J. (2020)**. "The WEIRDest People in the World" - Institutional origins of compliance behavior
2. **Lerer, I.A. (2025)**. "Beyond WEIRD Legal AI" - Concept-based vs token-based for non-WEIRD contexts  
3. **Jiang, Z. et al. (2025)**. "Paris: A Decentralized Trained Open-Weight Diffusion Model" - Technical foundation
4. **LegalGapDB Cases** - Real-world enforcement gap documentation

### Key Insights
- **WEIRD bias**: 12% of humanity creates AI models for 100% of use cases
- **Enforcement gaps**: Systematic differences between formal law and practice in 88% of jurisdictions  
- **Concept superiority**: Concept-based models capture cultural-institutional context better than token-based
- **Decentralized efficiency**: Paris methodology enables 14× data and 16× compute savings

## 🛣️ Roadmap

### Phase 1: MVP (Current)
- [x] Router architecture & training pipeline
- [x] 3 core experts (27.401, Procurement, Labor)  
- [x] Legal output schema with gap analysis
- [ ] Basic API endpoints

### Phase 2: Full System
- [ ] 8 complete expert domains
- [ ] Advanced gap detection algorithms
- [ ] Real-time LegalGapDB integration
- [ ] Cross-jurisdiction expert coordination

### Phase 3: Research Extensions  
- [ ] Temporal gap evolution modeling
- [ ] Behavioral compliance prediction
- [ ] Multi-language expert training
- [ ] Federated expert networks

## 📄 Citation

```bibtex
@software{paris_scm_2025,
  title = {Paris-SCM: Decentralized Legal AI for Non-WEIRD Jurisdictions},
  author = {Lerer, Ignacio Adrian},
  year = 2025,
  url = {https://github.com/adrianlerer/LegalGapDB/tree/main/scm_paris},
  note = {Based on Paris decentralized training framework}
}
```

## 🏛️ License & Ethics

- **Code**: MIT License (following Paris open-source commitment)
- **Legal Data**: CC BY-SA 4.0 (ensuring academic access)  
- **Ethical Commitment**: AI systems serving the Global Majority, not just WEIRD contexts
- **Transparency**: Open expert weights, training data, and gap detection methodology

---

*Building Legal AI that works for 88% of humanity living in non-WEIRD, post-colonial legal contexts*