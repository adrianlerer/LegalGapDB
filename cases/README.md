# 📁 Cases Directory

This directory contains the core database of legal gap cases documenting systematic divergences between formal law and informal practice in non-WEIRD jurisdictions.

## 🌍 Country Coverage

| Country | Cases | Status | Priority |
|---------|-------|--------|----------|
| 🇦🇷 **Argentina** | 20 | ✅ Seed Complete | High |
| 🇧🇷 **Brazil** | 0 | 🎯 Target Q2 2026 | High |
| 🇲🇽 **Mexico** | 0 | 🎯 Target Q3 2026 | High |
| 🇮🇳 **India** | 0 | 🎯 Target Q3 2026 | High |
| 🇳🇬 **Nigeria** | 0 | 🎯 Target Q4 2026 | Medium |

## 📊 Database Statistics

### Current Status
- **Total Cases**: 20
- **Countries**: 1
- **Legal Domains**: 5
- **Languages**: Spanish, English
- **Data Coverage**: 2024

### By Legal Domain
| Domain | AR | BR | MX | IN | NG | Total |
|--------|----|----|----|----|-------|
| Labor Law | 5 | 0 | 0 | 0 | 0 | **5** |
| Tax Law | 4 | 0 | 0 | 0 | 0 | **4** |
| Corporate Law | 4 | 0 | 0 | 0 | 0 | **4** |
| Criminal Law | 4 | 0 | 0 | 0 | 0 | **4** |
| Family Law | 2 | 0 | 0 | 0 | 0 | **2** |
| Administrative Law | 1 | 0 | 0 | 0 | 0 | **1** |
| **Total** | **20** | **0** | **0** | **0** | **0** | **20** |

## 🗂️ Directory Structure

```
cases/
├── README.md                    # This file
├── AR/                         # Argentina (20 cases)
│   ├── README.md               # Country overview
│   ├── labor/                  # Labor law cases (5)
│   ├── tax/                    # Tax law cases (4)
│   ├── corporate/              # Corporate law cases (4)
│   ├── criminal/               # Criminal law cases (4)
│   └── family/                 # Family law cases (2)
├── BR/                         # Brazil (planned Q2 2026)
├── MX/                         # Mexico (planned Q3 2026)
├── IN/                         # India (planned Q3 2026)
└── NG/                         # Nigeria (planned Q4 2026)
```

## 📋 Case Format

Each case follows a standardized JSON structure:

### Required Fields
- **case_id**: Format `XX-DOMAIN-NNN` (e.g., `AR-LAB-001`)
- **formal_rule**: Legal text with official citations
- **informal_practice**: Actual behavior with quantified gaps
- **gap_mechanism**: Causal explanation of why gap persists
- **english_abstract**: Summary for international researchers
- **metadata**: Contributor info, validation status, tags

### Data Quality Standards
- ✅ **Official sources**: Government statistics, academic studies
- ✅ **Quantified gaps**: Specific percentages and numbers
- ✅ **Current data**: Primarily 2024 information
- ✅ **Peer reviewed**: Expert validation for accuracy
- ✅ **Accessible citations**: Non-paywalled URLs when possible

## 🎯 Expansion Roadmap

### Phase 1: Argentina Foundation (✅ Complete)
- 20 seed cases across 5 legal domains
- Establishes methodology and quality standards
- Focuses on business/economic law areas

### Phase 2: Brazil Expansion (Q2 2026)
- Target: 50+ cases
- Priority domains: Labor, tax, environmental, corporate
- Portuguese language support
- Academic partnerships with USP, FGV

### Phase 3: Mexico & India (Q3 2026)
- Mexico: 40+ cases, focus on NAFTA compliance areas
- India: 60+ cases, emphasis on contract enforcement
- Multi-language support (Spanish, Hindi)
- Regional variation documentation

### Phase 4: Nigeria & Beyond (Q4 2026+)
- Nigeria: 30+ cases, natural resources and governance
- Additional countries based on contributor interest
- African legal systems representation
- Mobile data collection tools

## 📈 Quality Metrics

### Coverage Goals
- **500 total cases** by end of Year 1
- **10 legal domains** across all countries
- **80% high-confidence** cases with official data sources
- **90% current data** (2023-2025 timeframe)

### Validation Pipeline
1. **Submission**: Contributor uses templates
2. **Auto-validation**: Schema and citation checks
3. **Peer review**: Expert domain validation
4. **Editorial review**: Methodology compliance
5. **Publication**: DOI assignment and indexing

## 🤝 Contributing Cases

### Who Can Contribute
- 👨‍⚖️ **Legal practitioners** with local expertise
- 🎓 **Academic researchers** studying law and society
- 📊 **Policy analysts** with access to government data
- 🏛️ **Civil society** organizations tracking compliance

### Contribution Process
1. **Select target country/domain** from our priority list
2. **Review existing cases** in that jurisdiction
3. **Use our templates** in [`templates/`](../templates/)
4. **Submit via pull request** with complete documentation
5. **Participate in peer review** process

### Recognition
- Co-authorship credit on academic papers
- Listing in project contributors
- Speaking opportunities at conferences
- Collaboration on research grants

## 🔍 Research Applications

### Legal AI Training
- **Compliance prediction** models accounting for enforcement gaps
- **Risk assessment** tools for multinational corporations
- **Legal reasoning** systems that understand real-world practice

### Academic Research
- **Comparative legal studies** across jurisdictions
- **Law and economics** empirical analysis
- **Development studies** institution effectiveness research
- **Socio-legal studies** formal vs. informal law

### Policy Applications
- **Regulatory impact** assessment and design
- **International development** program targeting
- **Business strategy** for emerging markets
- **Legal reform** evidence base

## 📚 Documentation

### For Contributors
- [Contribution Guide](../CONTRIBUTING.md)
- [Case Templates](../templates/)
- [Validation Criteria](../validation/validation_criteria.md)
- [Style Guide](../docs/style_guide.md)

### For Researchers
- [API Documentation](../docs/api_reference.md)
- [Data Export Tools](../tools/)
- [Statistical Analysis](../research/benchmarks/)
- [Citation Guidelines](../CITATION.cff)

### For Developers
- [Schema Reference](../docs/schema_reference.md)
- [Validation Scripts](../tools/validate_case.py)
- [Export Utilities](../tools/export_corpus.py)

## ⚖️ Legal and Ethical Considerations

### Data Protection
- No personally identifiable information in cases
- Aggregate statistics only for sensitive topics
- Source protection in authoritarian contexts

### Academic Integrity
- Full attribution of data sources
- Transparent methodology documentation
- Peer review for quality assurance
- Open access with proper licensing

### Cultural Sensitivity
- Avoid legal imperialism and Western bias
- Collaborate with local experts
- Respect different legal traditions
- Acknowledge context and limitations

---

**Building Legal AI that works for 88% of humanity, not just the WEIRD 12%.**

*Last updated: February 2026*  
*Next milestone: Brazil expansion (Q2 2026)*