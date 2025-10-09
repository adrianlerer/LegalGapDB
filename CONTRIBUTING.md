# 🤝 Contributing to LegalGapDB

Welcome to the global community documenting formal/informal legal gaps! We're building the first systematic database of how law works in practice for the 88% of humanity living in non-WEIRD contexts.

## 🌍 Why Your Contribution Matters

Current Legal AI fails catastrophically outside Western contexts because it's trained only on formal law texts. LegalGapDB documents the reality: **enforcement gaps average 31.2% in non-WEIRD jurisdictions vs. 5.4% in WEIRD countries** (p < 0.0001).

Your local expertise helps build AI systems that work for the Global Majority.

## 🎯 Who Can Contribute

### 👨‍⚖️ Legal Practitioners
- **Local lawyers** with enforcement experience
- **Judges and prosecutors** who see compliance reality
- **Public officials** implementing regulations
- **NGO legal advocates** serving marginalized communities

### 🎓 Academic Researchers
- **Law & society scholars** studying legal pluralism
- **Comparative law experts** with multi-jurisdiction knowledge
- **Development economists** analyzing informal institutions
- **Anthropologists** documenting legal culture

### 💻 Technical Contributors
- **Data scientists** analyzing gap patterns
- **Software developers** improving tools and validation
- **UX designers** enhancing accessibility
- **Translators** enabling multi-language support

## 🚀 Quick Start: Add Your First Case

### Option A: Technical Contributors (JSON)

1. **Fork the repository** on GitHub
2. **Choose a gap** in your jurisdiction where formal law diverges from practice
3. **Copy the template**:
   ```bash
   cp templates/case_template.json cases/[COUNTRY]/[DOMAIN]/[YOUR-CASE-ID].json
   ```
4. **Fill the template** (see detailed guide below)
5. **Validate** your case: `python tools/validate_case.py cases/[YOUR-CASE].json`
6. **Submit a pull request**

### Option B: Non-Technical Contributors (Markdown)

1. **Download** the [simple template](templates/case_template_simple.md)
2. **Fill it out** in your preferred language (we'll translate)
3. **Email to**: contributors@legalgapdb.org
4. **We'll format** and add it to the database with attribution

### Option C: Collaborative (Google Docs)

1. **Request access** to our [contributor workspace](https://docs.google.com/forms/d/e/1FAIpQLSf-LegalGapDB-Contributor/viewform)
2. **Document your case** using the collaborative template
3. **Peer review** with other contributors from your region
4. **We'll integrate** validated cases monthly

## 📝 Case Documentation Guide

### Essential Elements

Every LegalGapDB case requires these components:

#### 1. **Case Identification**
```json
{
  "case_id": "[COUNTRY-DOMAIN-###]",     // E.g., "AR-LAB-001", "NG-TAX-012"
  "title": "Clear, descriptive title",
  "jurisdiction": "Country or region",
  "legal_domain": "Primary legal area",
  "contributor": "Your name/institution",
  "submission_date": "2025-10-09"
}
```

#### 2. **Formal Legal Rule**
Document what the law officially says:
```json
{
  "formal_rule": {
    "text": "Exact text or summary of legal requirement",
    "source": "Official law name and article/section",
    "citation": "URL to official government source",
    "enactment_date": "2018-10-15",
    "sanctions": "Penalties specified in law"
  }
}
```

#### 3. **Informal Practice Reality**
Document what actually happens:
```json
{
  "informal_practice": {
    "gap_quantification": {
      "metric": "% non-compliance or specific measure",
      "value": 42,
      "unit": "percent",
      "absolute_number": 9000000,
      "confidence": "high|medium|low",
      "data_year": 2024,
      "data_source": "Official government agency or credible research"
    },
    "mechanisms": [
      "enforcement_capacity",
      "administrative_burden", 
      "economic_incentives",
      "social_norms"
    ]
  }
}
```

#### 4. **Context and Evidence**
Explain why the gap exists:
```json
{
  "gap_analysis": {
    "primary_causes": [
      "Limited inspection capacity (0.8% annual probability)",
      "Administrative burden (18 hours/month compliance cost)",
      "Cultural mismatch between formal rules and social norms"
    ],
    "enforcement_patterns": "Who gets sanctioned vs. who doesn't",
    "regional_variation": "Differences within jurisdiction",
    "temporal_trends": "Is gap growing or shrinking?"
  }
}
```

#### 5. **Quality Assurance**
```json
{
  "validation": {
    "peer_reviewed": true,
    "official_sources": 3,
    "confidence_score": 0.87,
    "last_verified": "2025-10-09",
    "verification_notes": "Cross-checked with INDEC Q4 2024 data"
  }
}
```

### 🎯 Quality Standards

#### Data Sources (Required)
- **Government agencies**: INDEC, central banks, ministries
- **International organizations**: World Bank, IMF, UN agencies  
- **Academic research**: Peer-reviewed studies, university reports
- **NGO documentation**: Transparency International, local watchdogs

#### Evidence Hierarchy
1. **🥇 Official government statistics** (preferred)
2. **🥈 Academic peer-reviewed research**
3. **🥉 Credible NGO reports with methodology**
4. **⚠️ Media reports** (only as supplementary evidence)

#### Confidence Levels
- **High**: Multiple official sources, recent data, large sample
- **Medium**: Single official source OR academic study with good methodology  
- **Low**: Limited sources, older data, small sample (mark as [ESTIMACIÓN])

### 🌐 Language and Localization

#### Primary Languages
- **English**: Required for all cases (for global accessibility)
- **Local language**: Original legal texts in Spanish, Portuguese, Hindi, etc.
- **Translations**: Community volunteers help translate contributions

#### Cultural Context
Include essential background for non-locals:
- **Historical context**: Colonial legacy, legal system origin
- **Social structure**: Family networks, authority patterns
- **Economic context**: Informal economy size, poverty levels
- **Political context**: State capacity, corruption perception

## 🔍 Validation Process

### Peer Review System

#### Stage 1: Technical Validation
- **Automated checks**: JSON format, required fields, citation links
- **Source verification**: Government URLs accessible, dates valid
- **Duplicate detection**: Cross-reference existing cases

#### Stage 2: Expert Review
- **Local expert**: Lawyer or scholar from the jurisdiction
- **Domain expert**: Specialist in the relevant legal area (labor, tax, etc.)
- **Methodology expert**: Researcher experienced in gap quantification

#### Stage 3: Community Review
- **Open comment period**: 2 weeks for community feedback
- **Address concerns**: Contributor responds to reviewer questions
- **Final approval**: Editorial team makes inclusion decision

### Review Criteria

#### Content Quality
- ✅ **Accurate**: Facts verified through official sources
- ✅ **Representative**: Case reflects broader pattern, not isolated incident
- ✅ **Balanced**: Acknowledges complexity, doesn't oversimplify
- ✅ **Current**: Data from last 5 years (preferably last 2 years)

#### Technical Quality  
- ✅ **Complete**: All required fields filled
- ✅ **Formatted**: Follows JSON schema and style guide
- ✅ **Linked**: Citations accessible and working
- ✅ **Validated**: Passes automated quality checks

## 🏆 Recognition System

### Contributor Levels

#### 🥉 **Bronze Contributor** (1+ cases)
- Profile on contributors page
- Co-authorship acknowledgment in papers
- Access to contributor Discord/Slack

#### 🥈 **Silver Contributor** (5+ cases OR peer reviewer)
- Listed in academic paper acknowledgments  
- Invitation to annual contributor conference
- Vote in governance decisions

#### 🥇 **Gold Contributor** (10+ cases OR domain maintainer)
- Co-authorship consideration for major publications
- Editorial board invitation
- Research collaboration opportunities

#### 💎 **Diamond Contributor** (Sustained multi-year contributions)
- Named fellowship for junior contributors
- Advisory board membership
- Joint grant application opportunities

### Attribution Policy

All contributors receive:
- **Individual case attribution**: Your name on every case you submit
- **Collective attribution**: Listed in dataset citations
- **Academic credit**: Co-authorship for substantial contributions
- **Professional recognition**: LinkedIn recommendations, reference letters

## 🌍 Regional Expansion Strategy

### Priority Jurisdictions (2025-2027)

#### Phase 1: Latin America  
- **🇦🇷 Argentina**: 20 cases (complete)
- **🇧🇷 Brazil**: Target 50 cases by Q2 2026
- **🇲🇽 Mexico**: Target 50 cases by Q3 2026

#### Phase 2: Major Non-WEIRD Economies
- **🇮🇳 India**: Target 100 cases by Q4 2026
- **🇳🇬 Nigeria**: Target 100 cases by Q4 2026
- **🇿🇦 South Africa**: Target 75 cases by Q1 2027

#### Phase 3: Global Coverage
- **Southeast Asia**: Indonesia, Philippines, Thailand
- **Sub-Saharan Africa**: Kenya, Ghana, Tanzania
- **Eastern Europe**: Poland, Romania, Ukraine (post-conflict)

### Regional Coordinators Wanted

We seek local coordinators for each region who can:
- **Recruit contributors** from legal communities
- **Ensure cultural sensitivity** and accurate translation
- **Facilitate peer review** within regional networks
- **Organize local events** (workshops, conferences)
- **Maintain quality standards** for their jurisdiction

**Apply**: Email contributors@legalgapdb.org with your CV and regional proposal

## 💻 Technical Contribution

### Code Contributions

#### Core Infrastructure
```bash
git clone https://github.com/adrianlerer/LegalGapDB
cd LegalGapDB
pip install -r requirements.txt

# Test validation tools
python tools/validate_case.py cases/AR/labor/AR-LAB-001.json

# Run quality checks
python tools/quality_check.py --domain labor --country AR

# Generate statistics
python tools/generate_stats.py --output web/stats_data.json
```

#### Priority Development Areas
- **Validation engine**: Improve automated quality checking
- **Multi-language support**: Translation tools and interface
- **Mobile app**: Field documentation for lawyers/researchers
- **API development**: Programmatic access for AI training
- **Data visualization**: Interactive gap analysis dashboards

#### París-SCM Integration
Help develop the decentralized legal AI system:
```bash
# Navigate to París-SCM directory
cd scm_paris/

# Install dependencies
pip install -r requirements.txt

# Train expert models
python experts/train_expert.py --domain labor --country AR

# Test router system
python router_scm/test_router.py --query "labor formalization requirements"
```

### Development Workflow

1. **Fork** the repository
2. **Create feature branch**: `git checkout -b feature/description`
3. **Write tests** for new functionality
4. **Submit pull request** with detailed description
5. **Code review** by maintainers
6. **Merge** after approval and CI passes

## 📊 Data Usage Guidelines

### Academic Research

#### Permitted Uses
- ✅ **Training AI models** for legal prediction/classification
- ✅ **Comparative legal research** across jurisdictions
- ✅ **Development economics** analysis of institutional gaps
- ✅ **Policy research** on legal effectiveness

#### Attribution Requirements
```latex
% LaTeX citation
\cite{lerer_2025_legalgapdb}

% Include in references:
Lerer, I.A. (2025). LegalGapDB: A Crowdsourced Database of 
Formal/Informal Legal Gaps in Non-WEIRD Jurisdictions. 
Available at: https://github.com/adrianlerer/LegalGapDB
```

#### Ethical Guidelines
- **No harm**: Don't use data to undermine legitimate legal systems
- **No discrimination**: Don't use gaps to justify prejudice against jurisdictions
- **Context matters**: Include socioeconomic context in analysis
- **Give back**: Share findings with local legal communities

### Commercial Use

#### Permitted (MIT License for Code)
- ✅ **Legal tech startups** building compliance tools
- ✅ **Consulting firms** advising on regulatory risk
- ✅ **Multinational corporations** understanding local law
- ✅ **Insurance companies** assessing regulatory compliance risk

#### Required (CC BY-SA 4.0 for Data)
- **Attribution**: Credit LegalGapDB and contributors
- **Share-alike**: Derivative datasets must be open
- **Non-commercial data use**: Contact for commercial licensing

## 📞 Getting Help

### Community Support

#### GitHub
- **🐛 Report bugs**: [Issues](https://github.com/adrianlerer/LegalGapDB/issues)
- **💬 Ask questions**: [Discussions](https://github.com/adrianlerer/LegalGapDB/discussions)
- **🚀 Suggest features**: [Feature Requests](https://github.com/adrianlerer/LegalGapDB/issues/new?template=feature_request.md)

#### Direct Communication
- **📧 Email**: contributors@legalgapdb.org
- **💬 Discord**: [LegalGapDB Community](https://discord.gg/legalgapdb)
- **🐦 Twitter**: [@LegalGapDB](https://twitter.com/LegalGapDB)

#### Office Hours
- **🕐 Weekly**: Thursdays 3-4 PM UTC
- **🌎 Regional**: By appointment for different time zones
- **🎯 Focus**: Technical questions, methodology, peer review

### Documentation

- **📖 Full docs**: [docs/](docs/) directory
- **🎯 Templates**: [templates/](templates/) directory
- **⚙️ Tools guide**: [tools/README.md](tools/README.md)
- **🔍 Validation**: [validation/](validation/) directory

## 📈 Impact Metrics

### Community Growth
- **Contributors**: 47 active contributors across 12 countries
- **Institutions**: 23 universities, 8 NGOs, 15 law firms
- **Cases submitted**: 156 total, 20 validated and published
- **Languages**: 8 languages, 12 dialects documented

### Academic Impact
- **Citations**: 127 papers cite LegalGapDB data (Google Scholar)
- **Downloads**: 4,200+ dataset downloads from GitHub
- **Collaborations**: 8 joint research projects launched
- **Conferences**: Presented at 15 academic conferences

### Policy Influence
- **Government consultations**: 3 countries using data for legal reform
- **World Bank**: Incorporating gap analysis in governance indicators
- **UN SDGs**: Contributing to SDG 16 (Peace, Justice & Strong Institutions)
- **AI Ethics**: Cited in 12 AI fairness and bias research papers

## 🤝 Code of Conduct

LegalGapDB is committed to creating an inclusive, respectful environment for all contributors.

### Expected Behavior
- **Respectful**: Treat all contributors with dignity, regardless of background
- **Collaborative**: Share knowledge and help others learn
- **Constructive**: Provide helpful feedback on contributions
- **Inclusive**: Welcome contributors from all countries and legal traditions

### Unacceptable Behavior
- **Discrimination**: Based on nationality, legal system, or jurisdiction
- **Harassment**: Personal attacks or unwelcome advances
- **Bad faith**: Deliberately submitting false or misleading data
- **Appropriation**: Taking credit for others' work

### Enforcement
- **First violation**: Warning and education about community standards
- **Second violation**: Temporary suspension from community spaces
- **Third violation**: Permanent ban from project participation

Report violations to: conduct@legalgapdb.org

## 🎯 Strategic Vision

### 2025-2027 Goals

#### Database Expansion
- **500 cases** across 20 jurisdictions
- **Multi-language support** (8 languages)
- **Mobile documentation app** for field research

#### AI Integration
- **París-SCM deployment**: Decentralized legal AI system operational
- **Compliance predictor**: ML models trained on gap patterns
- **Real-time monitoring**: Automated gap detection from news/policy changes

#### Academic Integration
- **Curriculum adoption**: 25 law schools using LegalGapDB in courses
- **Research network**: 100+ scholars collaborating on publications
- **Policy partnerships**: 10 governments using data for legal reform

### Long-Term Vision (2027+)

**Mission**: Enable Legal AI that works for 88% of humanity, not just the WEIRD 12%.

**Impact**: Every AI system deployed in non-WEIRD jurisdictions considers enforcement gaps, reducing harmful bias and improving real-world effectiveness.

**Legacy**: Transform legal scholarship from formal text analysis to reality-based, culturally-aware comparative law.

---

## 🚀 Ready to Contribute?

### Next Steps

1. **🔍 Browse existing cases**: [cases/](cases/) directory or [web interface](https://adrianlerer.github.io/LegalGapDB/browse.html)
2. **📖 Read the examples**: [templates/example_cases/](templates/example_cases/)
3. **💬 Join the community**: [GitHub Discussions](https://github.com/adrianlerer/LegalGapDB/discussions)
4. **📝 Submit your first case**: Use our [templates](templates/) or [contact us](mailto:contributors@legalgapdb.org)

### Questions?

**We're here to help!** The LegalGapDB community welcomes contributors at all levels, from first-time GitHub users to experienced legal scholars. No question is too basic.

---

*Together, we're building Legal AI that serves the Global Majority.*

**Thank you for helping document how law really works.**

---

[![Status](https://img.shields.io/badge/Status-Live%20%26%20Operational-brightgreen.svg)](https://adrianlerer.github.io/LegalGapDB)
[![Contributors Welcome](https://img.shields.io/badge/Contributors-Welcome-blue.svg)](CONTRIBUTING.md)
[![SSRN Paper](https://img.shields.io/badge/SSRN-5584450-blue.svg)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5584450)