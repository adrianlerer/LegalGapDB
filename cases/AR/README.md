# 🇦🇷 Argentina - Legal Gap Cases

This directory contains legal gap cases documented in Argentina, covering systematic divergences between formal law and informal practice.

## 📊 Current Cases: 20

### By Legal Domain

| Domain | Cases | Completion |
|--------|-------|------------|
| 👨‍💼 **Labor Law** | 5 | ✅ Complete |
| 💰 **Tax Law** | 4 | ✅ Complete |
| 🏢 **Corporate Law** | 4 | ✅ Complete |
| ⚖️ **Criminal Law** | 4 | ✅ Complete |
| 👨‍👩‍👧‍👦 **Family Law** | 2 | ✅ Complete |
| 📋 **Administrative Law** | 1 | 🔄 In Progress |

### Case Overview

#### Labor Law (`labor/`)
- **AR-LAB-001**: Informal Labor Registration Gap (42% unregistered workers)
- **AR-LAB-002**: Severance Payment Gap (42% receive full payment)
- **AR-LAB-003**: Working Hours Enforcement (38% exceed limits without compensation)
- **AR-LAB-004**: Minimum Wage Compliance (28% below SMVM)
- **AR-LAB-005**: Vacation Rights Usage (34% don't use full entitlement)

#### Tax Law (`tax/`)
- **AR-TAX-001**: VAT Evasion (32% tax gap)
- **AR-TAX-002**: Corporate Income Tax Gap (19.2% vs 35% effective rate)
- **AR-TAX-003**: Tax Withholding Compliance (27% non-compliance)
- **AR-TAX-004**: Property Tax Enforcement (64% effective collection rate)

#### Corporate Law (`corporate/`)
- **AR-CORP-001**: Corporate Compliance Law 27.401 (31% full implementation)
- **AR-CORP-002**: Board Independence Requirements (47% effective compliance)
- **AR-CORP-003**: Board Meeting Requirements (66% meet quarterly standards)
- **AR-CORP-004**: Audit Committee Effectiveness (41% functional committees)

#### Criminal Law (`criminal/`)
- **AR-CRIM-001**: Economic Crimes Conviction Rate ([ESTIMACIÓN: 23.1%] conviction rate)
- **AR-CRIM-002**: Corporate Bribery Enforcement (5.1% conviction rate)
- **AR-CRIM-003**: Money Laundering Prosecution (3.1% from ROS reports)
- **AR-CRIM-004**: Tax Fraud Criminal Cases (4.97% conviction rate)

#### Family Law (`family/`)
- **AR-FAM-001**: Child Support Enforcement (42% full compliance)
- **AR-FAM-002**: Alimony Payment Compliance (37% full compliance)

## 🔍 Key Patterns Identified

### Common Gap Mechanisms
1. **Enforcement Capacity Limitations**: Limited inspectors, courts, and administrative resources
2. **Economic Incentives**: Cost-benefit calculations favoring non-compliance
3. **Administrative Burden**: Complex procedures discouraging compliance
4. **Social Norms**: Cultural acceptance of informal practices
5. **Legal Ambiguity**: Unclear standards enabling evasion

### Sectoral Insights
- **Labor informality** affects 42% of workers, highest in construction (76.6%) and domestic work (77%)
- **Tax compliance** varies significantly by sector and firm size
- **Corporate governance** shows better compliance in listed vs. family companies
- **Criminal enforcement** suffers from long procedural delays and resource constraints
- **Family law** enforcement hampered by informal economy and weak collection mechanisms

## 📈 Aggregate Statistics

| Metric | Average | Range |
|--------|---------|--------|
| **Compliance Rate** | 58.3% | [EST: 23.1%] - 73.0% |
| **Detection Probability** | 15.2% | 0.1% - 85.0% |
| **Enforcement Success** | 34.7% | 5.0% - 89.0% |
| **Case Duration** | 3.8 years | 2.1 - 6.4 years |

## 🎯 Priority Areas for Expansion

1. **Environmental Law** - Industrial compliance, waste management
2. **Consumer Protection** - Advertising standards, warranty enforcement  
3. **Competition Law** - Antitrust enforcement, market dominance
4. **Administrative Law** - Public procurement, licensing procedures
5. **Contract Law** - Commercial dispute resolution, enforcement

## 🤝 How to Contribute

### Adding New Argentina Cases
1. Use case ID format: `AR-DOMAIN-NNN` (e.g., `AR-ENV-001`)
2. Follow our [JSON template](../../templates/case_template.json)
3. Ensure citations from official sources (InfoLEG, INDEC, government agencies)
4. Include quantified gap measurements with confidence levels
5. Submit via pull request with peer review

### Domain Abbreviations
- `LAB` - Labor Law
- `TAX` - Tax Law  
- `CORP` - Corporate Law
- `CRIM` - Criminal Law
- `FAM` - Family Law
- `ENV` - Environmental Law
- `CON` - Consumer Law
- `COMP` - Competition Law
- `ADM` - Administrative Law
- `CONTRACT` - Contract Law

## 📚 Key Sources

### Government Agencies
- **INDEC**: Labor and economic statistics
- **AFIP**: Tax compliance and collection data
- **Ministerio de Trabajo**: Labor inspection statistics  
- **CNV**: Corporate governance compliance
- **MPF**: Criminal prosecution statistics
- **Poder Judicial**: Court statistics and case outcomes

### Academic Institutions
- Universidad de Buenos Aires (UBA)
- Universidad Torcuato Di Tella (UTDT)
- Universidad del CEMA
- CONICET research institutes

### Professional Organizations
- Instituto Argentino de Ejecutivos de Finanzas (IAEF)
- Colegio de Abogados
- Consejos Profesionales de Ciencias Económicas

## ⚠️ Data Quality Notes

- **Confidence Levels**: Most cases rated "high" confidence based on official statistics
- **Geographic Scope**: Primarily national data; some regional variations noted
- **Temporal Coverage**: Data from 2024 unless otherwise specified
- **Language**: Original sources in Spanish; English abstracts provided
- **Peer Review**: All seed cases validated by expert contributor

## 🔗 Related Resources

- [Argentina Legal System Overview](../../docs/legal_systems/argentina.md)
- [Data Collection Methodology](../../docs/methodology/argentina_sources.md)
- [Validation Criteria](../../validation/validation_criteria.md)

---

*Last updated: October 2025*  
*Cases contributed by: Ignacio Adrian Lerer (Legal Expert)*  
*Next review: August 2026 (scheduled)*