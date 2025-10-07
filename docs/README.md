# 📚 LegalGapDB Documentation

Welcome to the comprehensive documentation for LegalGapDB - the first open-source database documenting formal/informal legal gaps in non-WEIRD jurisdictions.

## 🗂️ Documentation Index

### 🚀 Getting Started
- **[Quick Start Guide](getting_started.md)** - Get up and running in 5 minutes
- **[Contribution Guide](contribution_guide.md)** - How to contribute cases and data
- **[FAQ](faq.md)** - Frequently asked questions
- **[Installation](installation.md)** - Set up development environment

### 📖 Reference Materials
- **[Schema Reference](schema_reference.md)** - Complete field-by-field documentation
- **[API Reference](api_reference.md)** - Programmatic access documentation
- **[Case Templates](../templates/)** - Structured templates for new cases
- **[Validation Criteria](validation_process.md)** - Quality standards and review process

### 🔧 Technical Documentation
- **[Data Format Specification](data_format.md)** - JSON schema and structure
- **[Validation Process](validation_process.md)** - Peer review and quality control
- **[Export Tools](../tools/)** - Data export utilities and formats
- **[Statistics Dashboard](stats_dashboard.md)** - Analytics and reporting tools

### 🎯 Use Cases and Applications
- **[Legal AI Training](use_cases/legal_ai.md)** - Using data for machine learning
- **[Academic Research](use_cases/academic_research.md)** - Research applications
- **[Policy Analysis](use_cases/policy_analysis.md)** - Government and NGO use
- **[Commercial Applications](use_cases/commercial.md)** - Business intelligence

### 🌍 Jurisdictional Guides
- **[Argentina](jurisdictions/argentina.md)** - Legal system overview and sources
- **[Brazil](jurisdictions/brazil.md)** - Planned expansion (Q2 2026)
- **[Mexico](jurisdictions/mexico.md)** - Planned expansion (Q3 2026)
- **[India](jurisdictions/india.md)** - Planned expansion (Q3 2026)

### 🏛️ Project Governance
- **[Governance Structure](governance.md)** - Decision-making and oversight
- **[Roadmap](roadmap.md)** - Development timeline and milestones
- **[Changelog](changelog.md)** - Version history and updates
- **[Code of Conduct](../CODE_OF_CONDUCT.md)** - Community standards

### 🔬 Research and Analysis
- **[Methodology](methodology/)** - Data collection and analysis methods
- **[Quality Assurance](quality_assurance.md)** - Validation and verification
- **[Statistical Analysis](statistical_analysis.md)** - Patterns and insights
- **[Benchmarks](../research/benchmarks/)** - Performance evaluation

## 📊 Quick Navigation

### By User Type

#### 🎓 Researchers & Academics
- [Getting Started](getting_started.md) → [API Reference](api_reference.md) → [Academic Use Cases](use_cases/academic_research.md)
- [Data Export Tools](../tools/export_corpus.py) for analysis datasets
- [Statistical Analysis](statistical_analysis.md) for research insights

#### 👨‍⚖️ Legal Practitioners
- [Contribution Guide](contribution_guide.md) → [Case Templates](../templates/) → [Validation Process](validation_process.md)
- Focus on [jurisdictional guides](jurisdictions/) for your region
- [FAQ](faq.md) for common questions about legal interpretation

#### 💻 Developers & Engineers  
- [Installation](installation.md) → [API Reference](api_reference.md) → [Schema Reference](schema_reference.md)
- [Tools Documentation](../tools/) for data processing
- [Commercial Applications](use_cases/commercial.md) for business use cases

#### 🏛️ Policy Makers & NGOs
- [Policy Analysis Guide](use_cases/policy_analysis.md) → [Statistics Dashboard](stats_dashboard.md)
- [Governance Structure](governance.md) for transparency
- [Quality Assurance](quality_assurance.md) for data reliability

### By Task

#### 📝 Contributing Cases
1. Read [Contribution Guide](contribution_guide.md)
2. Select appropriate [Case Template](../templates/case_template.json)
3. Follow [Validation Criteria](validation_process.md)
4. Submit via [GitHub process](../CONTRIBUTING.md)

#### 📊 Analyzing Data
1. Use [Export Tools](../tools/export_corpus.py) to get datasets
2. Review [Statistical Analysis](statistical_analysis.md) for patterns
3. Check [API Reference](api_reference.md) for programmatic access
4. See [Use Cases](use_cases/) for analysis examples

#### 🔧 Building Applications
1. Start with [Installation](installation.md)
2. Review [API Reference](api_reference.md) and [Schema](schema_reference.md)
3. Check [Commercial Applications](use_cases/commercial.md) guide
4. Use [Validation Tools](../tools/validate_case.py) for quality control

## 🌟 Key Concepts

### What is a Legal Gap?
A **legal gap** is a systematic divergence between:
- **Formal Rule**: What the law officially says
- **Informal Practice**: What actually happens in reality

### Why Does This Matter?
- 88% of humanity lives in non-WEIRD jurisdictions where such gaps are common
- Current Legal AI systems fail when deployed in these contexts
- Understanding gaps enables better policy and technology design

### Quality Standards
- **Official Sources**: Government statistics, academic studies
- **Quantified Gaps**: Specific numbers and percentages
- **Peer Review**: Expert validation for accuracy
- **Current Data**: Primarily 2023-2024 information

## 🔗 External Resources

### Academic Papers
- Henrich, J. et al. (2010). "The Weirdest People in the World?" *Behavioral and Brain Sciences*
- Hadfield, G. (2016). "Rules for a Flat World" - Oxford University Press
- Our forthcoming paper: "Beyond WEIRD Legal AI" (2026)

### Legal Databases
- **Argentina**: InfoLEG, SAIJ, INDEC
- **International**: World Bank Legal Database, OECD Legal Indicators
- **Academic**: HeinOnline, Westlaw International

### Technical Resources
- [JSON Schema Specification](https://json-schema.org/)
- [OpenAPI Documentation](https://swagger.io/specification/)
- [Creative Commons Licensing](https://creativecommons.org/licenses/)

## ❓ Getting Help

### Community Support
- **GitHub Discussions**: [Community Q&A](https://github.com/adrianlerer/LegalGapDB/discussions)
- **Issues**: [Bug Reports & Features](https://github.com/adrianlerer/LegalGapDB/issues)
- **Email**: adrian@lerer.com.ar for direct contact

### Contribution Opportunities  
- **Case Documentation**: Add cases from your jurisdiction
- **Translation**: Help with multi-language support
- **Code**: Improve tools and infrastructure
- **Research**: Collaborate on academic papers

### Office Hours
**Virtual office hours** every Friday 15:00-16:00 UTC (Argentina timezone)
- Zoom link posted in [Discussions](https://github.com/adrianlerer/LegalGapDB/discussions)
- No registration required - just bring your questions!

## 📋 Documentation Status

| Section | Status | Last Updated | Next Review |
|---------|--------|--------------|-------------|
| Getting Started | ✅ Complete | 2026-02-01 | 2026-05-01 |
| API Reference | ✅ Complete | 2026-02-01 | 2026-03-01 |
| Schema Reference | ✅ Complete | 2026-02-01 | 2026-04-01 |
| Use Cases | 🔄 In Progress | 2026-02-01 | 2026-03-01 |
| Jurisdictional Guides | 🔄 Partial | 2026-02-01 | 2026-04-01 |
| Tools Documentation | ✅ Complete | 2026-02-01 | 2026-06-01 |

## 🏷️ Tags and Categories

**Documentation Tags**: #getting-started #api #schema #validation #export #analysis #research #legal-ai #policy

**Difficulty Levels**:
- 🟢 **Beginner**: Getting Started, FAQ, Basic Use Cases
- 🟡 **Intermediate**: API Reference, Case Contribution, Analysis Tools  
- 🔴 **Advanced**: Schema Development, Tool Modification, Research Methods

---

*This documentation is maintained by the LegalGapDB community. Found an error or want to contribute? See our [contribution guidelines](../CONTRIBUTING.md).*

**Last Updated**: February 2026  
**Version**: 1.0  
**License**: CC BY-SA 4.0 (Documentation), MIT (Code)