# 🚀 Getting Started with LegalGapDB

Welcome! This guide will get you up and running with LegalGapDB in just 5 minutes. Whether you're a researcher, legal practitioner, or developer, we'll show you how to start exploring and contributing to the database.

## 🎯 What You'll Learn

- How to browse and search existing cases
- How to download data for your research
- How to contribute your first legal gap case
- How to validate and use the tools

## 📊 Step 1: Explore Existing Cases

### Online Browser (Easiest)
Visit **[legalgapdb.org/browse](https://legalgapdb.org/browse)** to:
- Browse cases by country and legal domain
- Search by keywords and tags
- View detailed case information
- Download individual cases or datasets

### GitHub Repository
Explore cases directly in our [GitHub repository](https://github.com/adrianlerer/LegalGapDB):

```bash
# Clone the repository
git clone https://github.com/adrianlerer/LegalGapDB.git
cd LegalGapDB

# Browse Argentina cases
ls cases/AR/
# labor/  tax/  corporate/  criminal/  family/

# View a specific case
cat cases/AR/labor/AR-LAB-001.json
```

### Quick Case Overview
```bash
# See all 20 Argentina seed cases
find cases/AR -name "*.json" | head -5
```

**Example Cases to Check Out:**
- **AR-LAB-001**: Labor informality (40.1% unregistered workers)
- **AR-TAX-001**: VAT evasion (32% tax gap)
- **AR-CRIM-001**: Economic crimes (23.1% conviction rate)

## 📥 Step 2: Download Data for Analysis

### Using Export Tools

```bash
# Install Python requirements
pip install -r tools/requirements.txt

# Export all cases as JSON Lines
python tools/export_corpus.py --format jsonl --output legalgap_data.jsonl

# Export Argentina cases as CSV for Excel analysis
python tools/export_corpus.py --format csv --filter-country AR --output argentina_cases.csv

# Export for machine learning (classification task)
python tools/export_corpus.py --format ml-classification --output training_data.jsonl
```

### Direct Downloads
- **[Complete Database (JSON)](https://github.com/adrianlerer/LegalGapDB/archive/main.zip)** - All cases and tools
- **[Argentina Dataset (CSV)](https://legalgapdb.org/downloads/argentina.csv)** - Spreadsheet-ready format
- **[Training Corpus (JSONL)](https://legalgapdb.org/downloads/training_corpus.jsonl)** - ML-optimized format

### Quick Analysis Example

```python
import pandas as pd
import json

# Load CSV export
df = pd.read_csv('argentina_cases.csv')

# Basic statistics
print(f"Total cases: {len(df)}")
print(f"Average compliance rate: {df['voluntary_compliance'].mean():.1f}%")
print(f"Domains covered: {df['legal_domain'].nunique()}")

# Gap distribution by domain
domain_gaps = df.groupby('legal_domain')['gap_value'].mean()
print("\nAverage gap by domain:")
print(domain_gaps.sort_values(ascending=False))
```

## 📝 Step 3: Contribute Your First Case

### Choose Your Case
Identify a law in your jurisdiction where:
- ✅ **Formal rule exists** (statute, regulation, etc.)
- ✅ **Compliance data available** (government stats, surveys)
- ✅ **Systematic gap** (not isolated incidents)
- ✅ **You have expertise** or reliable sources

**Good Examples:**
- Labor law compliance rates
- Tax collection vs. legal obligations
- Corporate governance requirements
- Environmental regulation enforcement

### Use Our Templates

#### Option 1: JSON Template (Structured)
```bash
# Copy the template
cp templates/case_template.json cases/XX/domain/XX-DOMAIN-001.json

# Edit with your data
# Follow the inline comments and examples
```

#### Option 2: Simple Markdown (Beginners)
```bash
# Use the beginner-friendly template
cp templates/case_template_simple.md my_case_draft.md

# Fill out in plain text, we'll help convert to JSON
```

### Essential Information Needed

1. **Formal Rule**
   - Legal text in original language
   - Official citation with URL
   - Enactment date

2. **Informal Practice** 
   - Current compliance statistics
   - Data sources (government, academic)
   - Geographic/sectoral breakdown

3. **Gap Mechanism**
   - Why the gap persists
   - Supporting evidence
   - Quantitative data when possible

### Example: Quick Case Structure

```json
{
  "case_id": "MX-LAB-001",
  "title": "Minimum Wage Compliance in Mexico",
  "jurisdiction": "Mexico",
  "legal_domain": "Labor Law",
  
  "formal_rule": {
    "text": "Ley Federal del Trabajo establece salario mínimo de $248.93 MXN diarios...",
    "citation": "https://www.gob.mx/conasami/documentos/tabla-de-salarios-minimos",
    // ... more fields
  },
  
  "informal_practice": {
    "text": "Según INEGI, 42% de trabajadores recibe menos del salario mínimo legal...",
    "gap_quantification": {
      "metric": "Percentage receiving below minimum wage",
      "value": 42.0,
      "confidence": "high",
      "data_year": 2024
    }
    // ... more fields
  }
  // ... rest of structure
}
```

## ✅ Step 4: Validate and Submit

### Validate Your Case
```bash
# Check your case against schema
python tools/validate_case.py cases/XX/domain/XX-DOMAIN-001.json

# Should show: ✅ XX-DOMAIN-001.json: PASSED
```

### Submit via GitHub
```bash
# Create branch for your case
git checkout -b case/XX-DOMAIN-001

# Add and commit
git add cases/XX/domain/XX-DOMAIN-001.json
git commit -m "Add XX-DOMAIN-001: Brief case description"

# Push and create pull request
git push origin case/XX-DOMAIN-001
# Then create PR on GitHub
```

### Peer Review Process
1. **Automatic validation** - Schema and citation checks
2. **Expert review** - Domain specialists validate accuracy  
3. **Editorial review** - Methodology compliance
4. **Publication** - DOI assignment and indexing

## 🛠️ Step 5: Use the Tools

### Generate Statistics Report
```bash
# Create HTML dashboard
python tools/stats_dashboard.py --format html --output report.html

# Open report.html in browser to see visualizations
```

### Advanced Export Options
```bash
# Export with specific filters
python tools/export_corpus.py \
  --format excel \
  --filter-country AR \
  --filter-domain "Labor Law" \
  --output argentina_labor.xlsx

# Export for regression analysis
python tools/export_corpus.py \
  --format ml-regression \
  --output compliance_prediction_data.jsonl
```

### API Access (Coming Soon)
```python
# Future API usage
import legalgapdb

client = legalgapdb.Client(api_key='your_key')
cases = client.cases.filter(country='AR', domain='Labor Law')
compliance_data = client.analytics.compliance_by_sector()
```

## 🎓 Next Steps

### For Researchers
1. **Read**: [Academic Use Cases](use_cases/academic_research.md)
2. **Download**: Complete dataset for analysis
3. **Cite**: Use our [citation format](../CITATION.cff)
4. **Collaborate**: Join our research network

### For Legal Practitioners  
1. **Contribute**: Cases from your jurisdiction
2. **Review**: Peer review existing cases
3. **Network**: Connect with global legal experts
4. **Learn**: Comparative legal insights

### For Developers
1. **Install**: Full development environment
2. **Explore**: [API Reference](api_reference.md) and [Schema](schema_reference.md)
3. **Build**: Applications using our data
4. **Contribute**: Improve tools and infrastructure

### For Policy Makers
1. **Analyze**: Patterns in your jurisdiction
2. **Compare**: International best practices  
3. **Evidence**: Data for policy decisions
4. **Monitor**: Enforcement effectiveness

## 📚 Essential Reading

- **[Case Templates](../templates/)** - Structured contribution formats
- **[Validation Process](validation_process.md)** - Quality assurance details
- **[FAQ](faq.md)** - Common questions answered
- **[Contributing Guide](../CONTRIBUTING.md)** - Detailed contribution process

## ❓ Common First Questions

### "How do I know if my case is suitable?"
- Does it show systematic non-compliance (not just isolated incidents)?
- Do you have reliable quantitative data on the gap?
- Can you explain WHY the gap persists?

### "What if I'm not a lawyer?"
- Non-lawyers welcome! We need economists, political scientists, sociologists
- Focus on empirical data and social science analysis
- Partner with local legal experts for formal rule interpretation

### "How detailed should my case be?"
- Minimum: Basic structure with quantified gap and one mechanism
- Better: Multiple data sources, sectoral breakdown, academic references
- Best: Comprehensive analysis with detailed quantitative evidence

### "What about sensitive jurisdictions?"
- We prioritize contributor safety
- Use aggregate data only, no personal information
- Consider anonymous contribution options
- Consult our [safety guidelines](safety_guidelines.md)

## 🤝 Getting Help

### Immediate Support
- **💬 GitHub Discussions**: [Community Q&A](https://github.com/adrianlerer/LegalGapDB/discussions)
- **🐛 Issues**: [Bug reports & feature requests](https://github.com/adrianlerer/LegalGapDB/issues)
- **📧 Email**: adrian@lerer.com.ar

### Office Hours
**Every Friday 15:00-16:00 UTC** (Argentina timezone)
- Drop-in virtual session
- Zoom link in [Discussions](https://github.com/adrianlerer/LegalGapDB/discussions)
- Bring your questions about cases, tools, or research

### Community
- **Twitter**: [@LegalGapDB](https://twitter.com/LegalGapDB) for updates
- **LinkedIn**: Follow our project page for professional network
- **Newsletter**: Monthly updates on new cases and research

---

## 🎉 Ready to Get Started?

1. **Explore** some existing cases to understand the format
2. **Download** data relevant to your interests  
3. **Identify** a legal gap in your area of expertise
4. **Contribute** using our templates and tools
5. **Join** our community of researchers and practitioners

**Welcome to LegalGapDB - helping build Legal AI that works for 88% of humanity! 🌍**