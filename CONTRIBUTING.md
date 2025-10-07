# 🤝 Contributing to LegalGapDB

Welcome! We're building the first comprehensive database of formal/informal legal gaps for the 88% of humanity living in non-WEIRD jurisdictions. Your contribution helps enable Legal AI that works for the Global Majority.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Types of Contributions](#types-of-contributions)
- [Getting Started](#getting-started)
- [Contributing Legal Cases](#contributing-legal-cases)
- [Code Contributions](#code-contributions)
- [Documentation](#documentation)
- [Peer Review Process](#peer-review-process)
- [Recognition](#recognition)
- [Getting Help](#getting-help)

## 📜 Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. Please report unacceptable behavior to adrian@lerer.com.ar.

## 🎯 Types of Contributions

### 🏛️ Legal Cases (Most Needed!)
Document formal/informal gaps in your jurisdiction:
- Labor law enforcement gaps
- Tax compliance patterns  
- Corporate governance divergence
- Criminal law enforcement rates
- Family law compliance issues

### 💻 Code & Tools
- Validation scripts
- Data export utilities
- Website improvements
- API development
- Mobile app features

### 📚 Documentation
- Translation to local languages
- Usage guides
- Academic papers
- Case study examples

### 🔍 Peer Review
- Validate case accuracy
- Check citation accessibility  
- Verify quantifications
- Assess methodology

## 🚀 Getting Started

### 1. Set Up Your Environment

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/LegalGapDB.git
cd LegalGapDB

# Install validation tools
pip install -r tools/requirements.txt

# Validate your setup
python tools/validate_case.py cases/AR/labor/AR-LAB-001.json
```

### 2. Choose Your Contribution Type

- **Legal Practitioner?** → Start with [Legal Cases](#contributing-legal-cases)
- **Developer?** → Check our [Issues](https://github.com/adrianlerer/LegalGapDB/issues) labeled `good-first-issue`
- **Researcher?** → Review our [research guidelines](docs/research_partnerships.md)
- **Translator?** → Help with [internationalization](docs/i18n_guide.md)

## ⚖️ Contributing Legal Cases

### Step-by-Step Process

#### 1. 🔍 Identify a Legal Gap

Look for laws where:
- **Formal rule exists** but compliance is systematically low
- **Quantifiable data** is available (surveys, government stats, academic studies)
- You have **local expertise** or reliable sources
- The gap **affects many people** (not just isolated incidents)

**Good examples:**
- Labor registration requirements vs. informal employment rates
- Tax obligations vs. actual collection rates
- Corporate governance rules vs. compliance surveys

**Avoid:**
- Anecdotal cases without data
- Laws with recent major changes
- Highly contested legal interpretations

#### 2. 📋 Choose Your Template

| Template | Best For | Difficulty |
|----------|----------|------------|
| [JSON Template](templates/case_template.json) | Structured, complete cases | Advanced |
| [YAML Alternative](templates/case_template.yaml) | Cleaner syntax | Intermediate |
| [Markdown Simple](templates/case_template_simple.md) | Quick documentation | Beginner |

#### 3. 📝 Document the Case

**Required Information:**

- **Formal Rule**: 
  - Original language text
  - Official citation with URL
  - Enactment/amendment dates
  
- **Informal Practice**:
  - Current compliance statistics
  - Reliable data sources  
  - Geographic/sectoral breakdown
  
- **Gap Mechanism**:
  - Why the gap persists (enforcement, incentives, norms)
  - Supporting evidence
  - Academic references if available

- **English Abstract**:
  - Brief summary for international researchers
  - Key numbers and patterns

**Quality Standards:**
- ✅ Cite official government sources when possible
- ✅ Include confidence levels for statistics
- ✅ Use specific numbers, not approximations
- ✅ Provide accessible URLs (not paywalled)
- ❌ Don't rely solely on news articles
- ❌ Don't include personal opinions as facts

#### 4. 🔬 Validate Your Case

```bash
# Check JSON structure and required fields  
python tools/validate_case.py your_case.json

# Verify citations are accessible
python tools/citation_checker.py your_case.json

# Review against our criteria
python tools/quality_check.py your_case.json
```

#### 5. 📤 Submit for Review

1. **Create a branch**: `git checkout -b case/XX-DOMAIN-NNN`
2. **Add your case**: Place in appropriate `cases/COUNTRY/domain/` directory
3. **Commit**: `git commit -m "Add XX-DOMAIN-NNN: Brief title"`
4. **Push**: `git push origin case/XX-DOMAIN-NNN`
5. **Open PR**: Use our [case submission template](.github/pull_request_template.md)

### Case ID Format

Use the pattern: `XX-DOMAIN-NNN`

- **XX**: ISO 3166-1 alpha-2 country code
- **DOMAIN**: Abbreviated legal domain
- **NNN**: Sequential 3-digit number

**Examples:**
- `AR-LAB-001` (Argentina Labor Law case 1)
- `BR-TAX-015` (Brazil Tax Law case 15)
- `IN-CORP-003` (India Corporate Law case 3)

**Domain Abbreviations:**
- `LAB` - Labor Law
- `TAX` - Tax Law  
- `CORP` - Corporate Law
- `CRIM` - Criminal Law
- `FAM` - Family Law
- `PROP` - Property Law
- `ENV` - Environmental Law
- `CON` - Consumer Law
- `ADM` - Administrative Law
- `CONTRACT` - Contract Law

## 💻 Code Contributions

### Development Setup

```bash
# Install development dependencies
pip install -r tools/requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
python -m pytest tests/
```

### Code Standards

- **Python**: Follow PEP 8, use type hints
- **JavaScript**: Use ES6+, follow Airbnb style guide
- **Documentation**: Docstrings for all functions
- **Testing**: Write tests for new features

### Priority Areas

1. **Validation Tools** - Better schema validation, citation checking
2. **Export Utilities** - More output formats (JSONL, CSV, XML)
3. **Analytics Dashboard** - Contribution statistics, gap patterns
4. **Mobile App** - Field data collection for researchers
5. **API Development** - REST API for programmatic access

## 📚 Documentation

### Writing Guidelines

- **Clear language** - Avoid legal jargon when possible
- **Examples** - Include concrete examples
- **Multilingual** - Key documents in Spanish, Portuguese, English
- **Accessible** - Follow WCAG 2.1 AA guidelines

### Translation Priorities

1. **Spanish** - Argentina, Mexico, Colombia cases
2. **Portuguese** - Brazil cases and documentation
3. **Hindi** - India cases and interface
4. **French** - West Africa expansion preparation

## 👥 Peer Review Process

### For Reviewers

**Qualifications:**
- Legal expertise in the relevant jurisdiction
- Academic credentials or professional experience
- Previous contributions to LegalGapDB (after initial bootstrap)

**Review Criteria:**
1. **Accuracy** - Are facts and citations correct?
2. **Completeness** - All required fields properly filled?
3. **Methodology** - Sound approach to gap quantification?
4. **Sources** - Reliable, accessible, recent data?
5. **Impact** - Significant gap affecting many people?

**Review Process:**
1. Assigned automatically based on expertise
2. 2 reviewers per case minimum  
3. 7-day review period
4. Consensus required for approval

### Review Checklist

- [ ] Case ID follows format (XX-DOMAIN-NNN)
- [ ] Formal rule has official citation
- [ ] Citations are accessible (not broken links)
- [ ] Quantification includes confidence level
- [ ] Gap mechanism is plausible and supported
- [ ] English abstract is accurate
- [ ] Metadata is complete

## 🏆 Recognition

### Contributor Levels

| Level | Requirements | Benefits |
|-------|--------------|----------|
| **Contributor** | 1+ accepted case | Listed in CONTRIBUTORS.md |
| **Reviewer** | 5+ quality reviews | Can approve cases |
| **Expert** | 10+ cases in domain | Badge on profile |
| **Maintainer** | Significant code contribution | Commit access |

### Awards

- **📊 Data Pioneer**: First case in new jurisdiction
- **🔍 Quality Guardian**: 50+ thorough reviews
- **🌐 Global Contributor**: Cases in 3+ countries
- **🛠️ Tool Builder**: Major code contribution
- **📚 Documentation Hero**: Significant writing contribution

### Academic Credit

- Co-authorship on papers using your contributed cases
- Citation credit in derivative research
- Speaking opportunities at conferences
- Collaboration on grant proposals

## ❓ Getting Help

### Quick Questions

- **💬 GitHub Discussions**: [Community Q&A](https://github.com/adrianlerer/LegalGapDB/discussions)
- **📱 WhatsApp**: Ask for contact details in Discussions (for field researchers)

### Technical Issues

- **🐛 Bug reports**: [GitHub Issues](https://github.com/adrianlerer/LegalGapDB/issues)
- **💡 Feature requests**: Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.yml)

### Email Contact

- **📧 General inquiries**: adrian@lerer.com.ar
- **🎓 Academic partnerships**: adrian@lerer.com.ar  
- **💼 Commercial licensing**: adrian@lerer.com.ar

### Office Hours

**Virtual office hours** every Friday 15:00-16:00 UTC (Argentina timezone)
- Zoom link posted in [Discussions](https://github.com/adrianlerer/LegalGapDB/discussions)
- No registration required
- Bring your questions!

---

## 🎯 Next Steps

Ready to contribute? Here's what to do:

1. **👀 Browse existing cases** in [`cases/`](cases/) to understand our format
2. **📖 Read the templates** in [`templates/`](templates/)
3. **🔍 Check our roadmap** in [`docs/roadmap.md`](docs/roadmap.md)  
4. **💬 Join the discussion** in [GitHub Discussions](https://github.com/adrianlerer/LegalGapDB/discussions)
5. **📝 Submit your first contribution**!

**Remember:** Every case you contribute helps build Legal AI that works for the Global Majority. Together, we're making law more accessible and AI more inclusive.

---

*Questions not answered here? Check our [FAQ](docs/faq.md) or reach out to adrian@lerer.com.ar*