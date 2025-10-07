# 🌍 LegalGapDB

[![License: Dual](https://img.shields.io/badge/License-Dual%20(CC--BY--SA%204.0%20%2B%20MIT)-blue.svg)](LICENSE.md)
[![Cases](https://img.shields.io/badge/Cases-20-green.svg)](cases/)
[![Contributors](https://img.shields.io/github/contributors/adrianlerer/LegalGapDB.svg)](https://github.com/adrianlerer/LegalGapDB/graphs/contributors)
[![Build Status](https://github.com/adrianlerer/LegalGapDB/workflows/Validate%20Cases/badge.svg)](https://github.com/adrianlerer/LegalGapDB/actions)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

**The first open-source database documenting formal/informal legal gaps in non-WEIRD jurisdictions.**

---

## 🎯 Mission

88% of humanity lives in countries where written law diverges systematically from legal practice. Current Legal AI systems trained on formal legal texts fail catastrophically when deployed in these jurisdictions because they ignore the **enforcement gap** - the systematic difference between what the law says and what actually happens.

LegalGapDB documents this gap to enable Legal AI that works for the **Global Majority**.

## 📊 Current Status

- **🇦🇷 20 seed cases** covering Argentina across 5 legal domains
- **🌎 5 target countries** (Argentina, Brazil, Mexico, India, Nigeria)
- **🎯 500 case target** for Year 1
- **📖 Dual licensing** (CC BY-SA 4.0 for data, MIT for code)

### Cases by Domain
| Domain | Argentina | Brazil | Mexico | India | Nigeria | Total |
|--------|-----------|--------|--------|-------|---------|-------|
| Labor Law | 5 | 0 | 0 | 0 | 0 | **5** |
| Tax Law | 4 | 0 | 0 | 0 | 0 | **4** |
| Corporate Law | 4 | 0 | 0 | 0 | 0 | **4** |
| Criminal Law | 4 | 0 | 0 | 0 | 0 | **4** |
| Family Law | 2 | 0 | 0 | 0 | 0 | **2** |
| Administrative Law | 1 | 0 | 0 | 0 | 0 | **1** |
| **Total** | **20** | **0** | **0** | **0** | **0** | **20** |

## 🚀 Quick Start

### 1. 🔍 Explore
Browse cases at **[legalgapdb.org/browse](https://legalgapdb.org/browse)** or directly in the [`cases/`](cases/) directory.

### 2. 📝 Contribute  
Use our [templates](templates/) to document a gap in your jurisdiction:
- 📋 [JSON Template](templates/case_template.json) (structured data)
- 📝 [Markdown Template](templates/case_template_simple.md) (for non-technical contributors)
- 📖 [Annotated Example](templates/example_cases/AR-LAB-001_annotated.json)

### 3. 🔬 Research
Download the dataset for your Legal AI project:
```bash
# Clone the repository
git clone https://github.com/adrianlerer/LegalGapDB.git

# Export as training corpus
python tools/export_corpus.py --format jsonl --output legalgap_corpus.jsonl

# Validate new cases
python tools/validate_case.py cases/AR/labor/AR-LAB-001.json
```

## 📖 Featured Case Example

<details>
<summary><strong>🇦🇷 AR-LAB-001: Informal Labor Registration Gap</strong> (Click to expand)</summary>

```json
{
  "case_id": "AR-LAB-001",
  "title": "Informal Labor: Registration and Social Security Gap",
  "jurisdiction": "Argentina",
  "legal_domain": "Labor Law",
  
  "formal_rule": {
    "text": "La Ley de Contrato de Trabajo establece que todo empleador debe registrar trabajadores en seguridad social dentro de 5 días...",
    "source": "Ley 20.744 - Ley de Contrato de Trabajo",
    "citation": "http://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm"
  },
  
  "informal_practice": {
    "gap_quantification": {
      "metric": "Percentage of workers without formal registration",
      "value": 40.1,
      "unit": "percent",
      "absolute_number": 4800000,
      "confidence": "high",
      "data_year": 2024
    }
  },
  
  "english_abstract": {
    "formal": "Argentine Labor Contract Law mandates employer registration of workers within 5 days and 23% salary contributions.",
    "informal": "40.1% of workers operate without registration, varying by sector: construction (58%), domestic work (72%).",
    "gap": "Gap persists due to limited inspection capacity (0.8% annual probability), administrative burden (18 hours/month), and selective enforcement."
  }
}
```

**Why this matters for AI:** Legal AI trained only on the formal rule would predict 100% compliance, but reality is 60% - a catastrophic error for any system deployed in Argentina.

</details>

## 📈 Statistics Dashboard

### Gap Distribution by Mechanism
- 🏛️ **Enforcement Capacity**: 35% of gaps
- 📋 **Administrative Burden**: 25% of gaps  
- 💰 **Economic Incentives**: 20% of gaps
- 👥 **Social Norms**: 15% of gaps
- 🤝 **Corruption**: 5% of gaps

### Compliance Rates by Domain
- ⚖️ **Labor Law**: 59.9% average compliance
- 💼 **Corporate Law**: 71.2% average compliance
- 💰 **Tax Law**: 68.5% average compliance
- 🏛️ **Criminal Law**: 23.1% conviction rate
- 👨‍👩‍👧‍👦 **Family Law**: 45.3% average compliance

*Updated: February 2026*

## 🤝 How to Contribute

We welcome contributions from:
- 👨‍⚖️ **Legal practitioners** with local expertise
- 🎓 **Researchers** studying law and society  
- 💻 **Developers** improving tools and infrastructure
- 📊 **Data scientists** analyzing patterns and gaps

### 4-Step Contribution Process

1. **🔍 Choose a gap** - Identify a law with systematic non-compliance
2. **📝 Document** - Use our [templates](templates/) to structure your case
3. **👥 Review** - Submit for [peer review](validation/peer_review_guide.md)
4. **🎉 Publish** - Get a DOI and join our contributor community

**Read the full [Contribution Guide](CONTRIBUTING.md)**

## 📚 Citation

### BibTeX
```bibtex
@dataset{lerer_2026_legalgapdb,
  author       = {Lerer, Ignacio Adrian},
  title        = {{LegalGapDB: A Crowdsourced Database of 
                   Formal/Informal Legal Gaps in Non-WEIRD 
                   Jurisdictions}},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://github.com/adrianlerer/LegalGapDB}
}
```

### APA
Lerer, I. A. (2026). *LegalGapDB: A Crowdsourced Database of Formal/Informal Legal Gaps in Non-WEIRD Jurisdictions* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

## 🏛️ Governance

LegalGapDB is governed by a **Scientific Advisory Committee** including:
- Legal scholars from target jurisdictions
- AI/ML researchers focused on fairness
- Practitioners with enforcement experience
- Community representatives

**Decision-making process:** [governance.md](docs/governance.md)

## 🗺️ Roadmap

### 🎯 Year 1 Milestones (2026)
- [x] **Q1**: Launch with 20 Argentina seed cases
- [ ] **Q2**: Expand to Brazil (50+ cases), add peer review system
- [ ] **Q3**: Add Mexico and India (100+ cases each)  
- [ ] **Q4**: Nigeria expansion, first academic paper, 500+ total cases

### 🚀 Future Vision (2027+)
- **Multi-language support** (Spanish, Portuguese, Hindi, Yoruba)
- **AI compliance predictor** trained on gap patterns
- **Mobile app** for field documentation
- **Academic partnerships** with law schools globally

**Full roadmap:** [roadmap.md](docs/roadmap.md)

## 📬 Contact

- **📧 Email**: legalgapdb@gmail.com
- **🐦 Twitter**: [@LegalGapDB](https://twitter.com/LegalGapDB)
- **💬 Issues**: [GitHub Issues](https://github.com/adrianlerer/LegalGapDB/issues)
- **📱 WhatsApp**: +54 9 11 xxxx-xxxx (for field researchers)

## 🙏 Acknowledgments

Special thanks to our **founding contributors**:
- Prof. Maria Santos (Universidad de Buenos Aires) - Labor Law expert
- Dr. Carlos Rodriguez (CONICET) - Legal anthropologist  
- Ana García (Ministerio de Trabajo) - Policy analyst
- The **Open Law Movement** community

**View all contributors:** [CONTRIBUTORS.md](CONTRIBUTORS.md)

---

## 📄 License

**Dual License:**
- 📊 **Dataset**: [CC BY-SA 4.0](LICENSE-DATA.md) - Share and adapt with attribution
- 💻 **Code**: [MIT](LICENSE-CODE.md) - Free for commercial use

## 🔗 Links

- **🌐 Website**: https://legalgapdb.org
- **📊 Browse Cases**: https://legalgapdb.org/browse  
- **📈 Statistics**: https://legalgapdb.org/stats
- **🤝 Contributors**: https://legalgapdb.org/leaderboard
- **📚 API Docs**: https://legalgapdb.org/api

---

*Building Legal AI that works for 88% of humanity, not just the WEIRD 12%.*

**Made with ❤️ by the global legal community**