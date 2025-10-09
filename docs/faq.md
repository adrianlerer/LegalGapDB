# ❓ Frequently Asked Questions

## 🎯 General Questions

### What is LegalGapDB?
LegalGapDB is the first open-source database documenting systematic divergences between formal law and informal practice in non-WEIRD jurisdictions. We focus on countries where written law differs significantly from legal reality.

### Why do legal gaps matter?
88% of humanity lives in countries where formal law and actual practice diverge systematically. Current Legal AI systems trained only on formal legal texts fail catastrophically when deployed in these contexts. Understanding gaps enables better AI, policy, and business decisions.

### What does "WEIRD" mean?
WEIRD stands for **Western, Educated, Industrialized, Rich, and Democratic** societies (primarily USA, Canada, Western Europe, Australia). Most legal AI research focuses on these jurisdictions, ignoring the other 88% of humanity.

### How is this different from existing legal databases?
- **Focus on gaps**: We document divergence, not just formal law
- **Quantified data**: Specific statistics on compliance rates and enforcement
- **Causal analysis**: We explain WHY gaps persist
- **Open source**: Free access with proper licensing
- **Global scope**: Non-WEIRD jurisdictions prioritized

## 📊 Data and Methodology

### How do you ensure data quality?
- **Official sources**: Government statistics, academic studies preferred
- **Peer review**: Expert validation by legal practitioners
- **Schema validation**: Automated checks for completeness
- **Citation verification**: URLs must be publicly accessible
- **Confidence levels**: All data tagged with reliability assessment

### What counts as a "legal gap"?
A legal gap requires:
1. **Formal rule**: Clear legal requirement (statute, regulation, etc.)
2. **Informal practice**: Different actual behavior with data
3. **Systematic pattern**: Not isolated incidents
4. **Quantifiable**: Statistics on compliance rates or enforcement

### Why focus on compliance rates instead of case law?
Case law shows what courts decide, but often doesn't reflect broader social reality. We're interested in how law actually functions in society, which requires empirical data on behavior and enforcement.

### How current is the data?
- **Preference**: 2023-2024 data
- **Acceptable**: 2020-2024 with explanation
- **Older data**: Only if it's the most recent available
- **Update cycle**: Cases reviewed annually for freshness

## 🤝 Contributing

### Who can contribute?
- **Legal practitioners** with local expertise
- **Academic researchers** studying law and society
- **Policy analysts** with access to government data
- **Civil society** organizations tracking compliance
- **Anyone** with reliable data and local knowledge

### Do I need to be a lawyer?
No! We welcome contributions from:
- **Economists** studying regulatory compliance
- **Political scientists** researching institutions
- **Sociologists** examining legal culture
- **Data scientists** analyzing government statistics
- **NGO researchers** monitoring enforcement

### What if my English isn't perfect?
- Write in your native language first, we can help translate
- Focus on getting the data and analysis right
- Our community includes multilingual reviewers
- Use our [simple markdown template](../templates/case_template_simple.md)

### How long does the review process take?
- **Automatic validation**: Immediate (schema check)
- **Peer review**: 2-4 weeks typical
- **Editorial review**: 1-2 weeks after peer approval
- **Total time**: Usually 4-8 weeks from submission to publication

### What if I disagree with a published case?
- **Challenge process**: Use our [case challenge form](.github/ISSUE_TEMPLATE/case_challenge.yml)
- **Evidence required**: Counter-data with sources
- **Expert review**: Independent assessment
- **Possible outcomes**: Update, dispute flag, or no change
- **Transparency**: All challenges and responses public

## 🔒 Legal and Ethical

### What about contributor safety?
- **Anonymous options**: Contact us for sensitive jurisdictions
- **Aggregate data only**: No personally identifiable information
- **Source protection**: We can help obscure contributor identity
- **Risk assessment**: We evaluate safety concerns case-by-case

### Can I use this data commercially?
**Yes, with conditions:**
- **Dataset**: CC BY-SA 4.0 - requires attribution and share-alike
- **Code**: MIT license - minimal restrictions
- **Commercial use**: Explicitly allowed with proper attribution
- **Examples**: Legal tech startups, consulting firms, multinational compliance

### What about government sensitivity?
- **Public data focus**: We prioritize already-public information
- **Academic freedom**: Research purposes protected
- **Factual reporting**: We document reality, not advocate positions
- **Transparency**: All sources and methods public

### How do you handle bias?
- **Multiple contributors**: Diverse perspectives required
- **Peer review**: Independent expert validation
- **Source diversity**: Multiple data sources preferred
- **Methodology transparency**: All methods documented
- **Challenge process**: Public dispute resolution

## 🛠️ Technical Questions

### What formats can I export data in?
- **JSON/JSONL**: Machine-readable structured data
- **CSV**: Spreadsheet analysis
- **Excel**: Multi-sheet analysis with summaries
- **ML formats**: Classification, regression, text generation
- **API**: Programmatic access (coming 2026 - planned)

### Can I download the entire database?
Yes! Multiple options:
- **GitHub**: Clone complete repository
- **Exports**: Use our export tools for specific formats
- **Releases**: Periodic snapshots with DOIs
- **API**: Bulk download endpoints (coming soon)

### How do I cite this database?
```bibtex
@dataset{lerer_2025_legalgapdb,
  author = {Lerer, Ignacio Adrian},
  title = {{LegalGapDB: A Crowdsourced Database of 
           Formal/Informal Legal Gaps in Non-WEIRD 
           Jurisdictions}},
  year = 2025,
  publisher = {Zenodo},
  doi = {10.5281/zenodo.PENDING}
}
```

### What's the API rate limit?
- **Current**: No API yet (direct downloads available)
- **Planned**: 1000 requests/hour for research use
- **Commercial**: Higher limits available by arrangement
- **Launch**: Q3 2026 estimated (planned)

## 🌍 Coverage and Expansion

### Which countries are included?
**Current (2026):**
- 🇦🇷 **Argentina**: 20 cases (complete seed dataset)

**Planned 2026:**
- 🇧🇷 **Brazil**: Q2 2026 (target: 50+ cases)
- 🇲🇽 **Mexico**: Q3 2026 (target: 40+ cases)  
- 🇮🇳 **India**: Q3 2026 (target: 60+ cases)
- 🇳🇬 **Nigeria**: Q4 2026 (target: 30+ cases)

### How do you choose which countries to include?
**Priority factors:**
- **Population size**: Large countries first
- **Economic importance**: Major emerging markets
- **Legal system diversity**: Different legal traditions
- **Contributor availability**: Local expert partners
- **Data availability**: Reliable government statistics

### Can I request my country be added?
Absolutely! We prioritize based on:
- **Local contributors**: Partners with expertise
- **Data availability**: Reliable sources
- **Community interest**: User demand
- **Strategic importance**: Regional representation

### What legal domains are covered?
**Current domains:**
- Labor Law, Tax Law, Corporate Law, Criminal Law, Family Law

**Planned additions:**
- Environmental Law, Consumer Protection, Competition Law
- Administrative Law, Contract Law, Property Law
- International Trade, Financial Regulation

## 🔬 Research Applications

### How can I use this for academic research?
**Example applications:**
- **Comparative law**: Cross-jurisdictional gap patterns
- **Law and economics**: Enforcement effectiveness analysis  
- **Development studies**: Institutional quality measurement
- **Legal AI**: Training compliance prediction models

### Are there research partnerships available?
Yes! We collaborate with:
- **Universities**: Joint research projects and funding
- **Think tanks**: Policy analysis and reform recommendations
- **International organizations**: World Bank, OECD, UN projects
- **Legal firms**: Comparative analysis for multinational clients

### Can I get early access to new data?
**Research partners** get:
- Pre-publication access to new cases
- Custom data exports and analysis
- Co-authorship opportunities
- Conference presentation slots

Contact adrian@lerer.com.ar for partnership discussions.

## 💼 Commercial Use

### Can law firms use this data?
**Yes!** Common applications:
- **Due diligence**: Understanding local enforcement reality
- **Risk assessment**: Compliance probability analysis
- **Client advice**: Realistic enforcement expectations
- **Market entry**: Regulatory environment analysis

### What about legal tech companies?
**Definitely!** Use cases:
- **AI training**: Realistic compliance prediction
- **Risk scoring**: Country/sector specific models
- **Decision support**: Gap-aware legal reasoning
- **Market intelligence**: Competitive compliance analysis

### Are there usage restrictions?
**Dataset (CC BY-SA 4.0):**
- ✅ Commercial use allowed
- ✅ Modification permitted
- ⚠️ Must share improvements
- ⚠️ Attribution required

**Code (MIT):**
- ✅ Commercial use
- ✅ Modification
- ✅ No sharing required
- ⚠️ Attribution appreciated

## 🤔 Conceptual Questions

### Isn't non-compliance always bad?
Not necessarily! Sometimes:
- **Laws are outdated**: Technology or society changed
- **Laws are impractical**: Implementation costs exceed benefits
- **Laws conflict**: Different regulations contradict
- **Social norms differ**: Cultural practices diverge from formal law

We document reality without moral judgment.

### How is this different from corruption studies?
**Broader scope:**
- **Corruption**: Illegal behavior by officials
- **Legal gaps**: Any formal/informal divergence
- **Includes**: Resource constraints, cultural factors, economic incentives
- **Neutral perspective**: Not necessarily illegal or immoral

### What about legal pluralism?
We acknowledge multiple legal systems coexist:
- **Formal law**: State-enacted rules
- **Customary law**: Traditional practices
- **Religious law**: Faith-based systems
- **Commercial law**: Industry practices

Our focus is formal-informal gaps, but we're sensitive to legal pluralism.

## 🔮 Future Plans

### What's on the roadmap?
**2026 Goals:**
- 500 total cases across 5 countries
- Multi-language interface (Spanish, Portuguese)
- REST API launch
- Academic partnerships

**2027+ Vision:**
- 10+ countries covered
- Mobile data collection app
- AI compliance predictor
- Policy impact analysis tools

### How can I stay updated?
- **Newsletter**: Monthly updates and new research
- **Twitter**: [@LegalGapDB](https://twitter.com/LegalGapDB)
- **GitHub**: Watch repository for releases
- **Email**: adrian@lerer.com.ar for direct updates

---

## 🆘 Still Have Questions?

### Community Support
- **💬 GitHub Discussions**: [Ask the community](https://github.com/adrianlerer/LegalGapDB/discussions)
- **🎓 Office Hours**: Every Friday 15:00-16:00 UTC
- **📧 Email**: adrian@lerer.com.ar

### Quick Links
- **[Getting Started](getting_started.md)** - 5-minute introduction
- **[Contributing Guide](../CONTRIBUTING.md)** - How to add cases
- **[API Reference](api_reference.md)** - Technical documentation
- **[Use Cases](use_cases/)** - Application examples

---

*Can't find your question? Ask in [GitHub Discussions](https://github.com/adrianlerer/LegalGapDB/discussions) and we'll add it to this FAQ!*