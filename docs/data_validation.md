# 📊 Data Validation Protocol - LegalGapDB

**Version:** 1.0  
**Last Updated:** October 7, 2025  
**Protocol:** Reality Reasoner 3.0

## 🎯 Purpose

This document establishes the **data verification protocol** for all statistical claims in LegalGapDB to ensure academic rigor and prevent the inclusion of unverified or incorrect data.

## ⚠️ Critical Requirements

### **NEVER include unverified statistical claims**
Every numerical assertion in LegalGapDB MUST be:
1. **Sourced** from an official, verifiable source
2. **Labeled** with confidence level  
3. **Dated** with data collection period
4. **Updated** when new data becomes available

---

## 📋 Verification Levels

### ✅ **[VERIFIED]** - Highest Confidence
- **Source**: Official government statistics
- **Accessibility**: Public, with direct URL/DOI
- **Recency**: Data <2 years old
- **Cross-validation**: Confirmed by multiple sources

**Example**: 
```json
"gap_quantification": {
  "value": 42,
  "confidence": "verified",
  "source": "INDEC EPH Q4 2024",
  "url": "https://www.indec.gob.ar/uploads/informesdeprensa/informalidad_laboral_eph_04_2529DEBE4DBB.pdf",
  "verification_date": "2025-10-07"
}
```

### ⚠️ **[ESTIMACIÓN]** - Medium Confidence  
- **Source**: Academic studies, professional estimates
- **Method**: Clearly documented methodology
- **Limitations**: Acknowledged uncertainty
- **Use case**: When official data unavailable but reasonable estimates exist

**Example**:
```json
"text": "[ESTIMACIÓN]: Según datos del MPF y el Poder Judicial, la tasa de condenas efectivas por delitos económicos es del 23.1%",
"confidence": "medium",
"note": "Estimate based on available MPF data - requires official verification"
```

### 🔴 **[CONJETURA]** - Low Confidence
- **AVOID**: Generally should not be included
- **Exception**: When properly contextualized as hypothesis
- **Requirement**: Must be clearly labeled and justified

---

## 🔍 Verification Process

### **Step 1: Source Identification**
For every statistical claim, identify:
- [ ] **Primary source** (government agency, research institution)
- [ ] **Publication date** and data collection period
- [ ] **Methodology** used to generate the statistic
- [ ] **Geographic scope** and sample size

### **Step 2: Source Verification**
- [ ] **URL check**: Confirm link is accessible and points to correct document
- [ ] **Institution verification**: Confirm source is legitimate official entity
- [ ] **Data consistency**: Check if numbers align with other reports from same source
- [ ] **Methodological review**: Assess if methodology is sound

### **Step 3: Cross-Validation**
- [ ] **Multiple sources**: Seek confirmation from at least 2 independent sources
- [ ] **Temporal consistency**: Check if trend aligns with historical data
- [ ] **International comparison**: Compare with similar countries when available
- [ ] **Expert consultation**: Consult domain experts when available

### **Step 4: Documentation**
- [ ] **Complete metadata**: Source, date, methodology, confidence level
- [ ] **Verification trail**: Document who verified and when
- [ ] **Update schedule**: Set date for next verification
- [ ] **Change log**: Track all updates with reasons

---

## 🚨 Common Verification Failures

### **Red Flags to Avoid:**
1. **Round numbers without explanation** (e.g., exactly 50% - suspicious)
2. **No source citation** or broken links
3. **Outdated data** (>3 years old) presented as current
4. **Conflicting statistics** within the same document
5. **Impossible precision** (e.g., 23.147% when methodology can't support such precision)

### **Examples of Past Corrections:**
- **Labor informality**: Updated from imprecise "40.1%" to verified "42%" (INDEC Q4 2024)
- **Sector breakdown**: Corrected construction from "58%" to verified "76.6%" (INDEC Q4 2024)  
- **Inspection rates**: Marked unverified "0.8%" as **[ESTIMACIÓN]** pending official data

---

## 🛠️ Tools and Resources

### **Verification Tools**
1. **Archive.org Wayback Machine**: For checking historical versions of sources
2. **Google Scholar**: For finding academic validation of statistics
3. **Government data portals**: Official statistical agencies by country
4. **International organizations**: World Bank, OECD, ILO data

### **Argentina-Specific Sources**
- **INDEC**: https://www.indec.gob.ar/ (labor, economic data)
- **AFIP**: https://www.afip.gob.ar/ (tax data)
- **MPF**: https://www.mpf.gob.ar/ (criminal justice data) 
- **Ministerio de Trabajo**: https://www.argentina.gob.ar/trabajo (labor enforcement)

### **Red Flag Detection Script**
```bash
#!/bin/bash
# Script to identify potential unverified statistics
cd /path/to/LegalGapDB
echo "=== Checking for unverified statistics ==="
grep -r "\b[0-9]+\.[0-9]%" cases/ | grep -v "\[VERIFIED\]" | grep -v "\[ESTIMACIÓN\]"
echo "=== Checking for missing sources ==="
grep -r "\"value\":" cases/ | xargs -I {} sh -c 'if ! grep -q "source" "{}"; then echo "Missing source: {}"; fi'
```

---

## 🔄 Update Protocol

### **Quarterly Reviews (Every 3 Months)**
- [ ] Check for new data releases from primary sources
- [ ] Update statistics that have newer versions available  
- [ ] Re-verify sources that may have changed URLs
- [ ] Update confidence levels based on new information

### **Annual Full Audit**
- [ ] Complete re-verification of all statistics
- [ ] Source methodology review for any changes
- [ ] Cross-validation with international databases
- [ ] Update all metadata and verification dates

### **Immediate Updates (When Issues Found)**
- [ ] **Within 24 hours**: Mark questionable data as **[ESTIMACIÓN]**
- [ ] **Within 1 week**: Find official replacement or remove
- [ ] **Document**: All changes in git commit messages
- [ ] **Notify**: Contributors and users of significant corrections

---

## 📝 Quality Assurance Checklist

Before submitting any case with statistical data:

### **Data Quality Check**
- [ ] Every statistic has official source citation
- [ ] All URLs are accessible and point to correct data
- [ ] Confidence levels are accurately assigned
- [ ] Data is <2 years old or properly contextualized if older
- [ ] Cross-validation attempted when possible

### **Metadata Completeness**
- [ ] Source institution clearly identified
- [ ] Data collection methodology documented
- [ ] Geographic and temporal scope specified  
- [ ] Verification date recorded
- [ ] Next update date scheduled

### **Consistency Check**
- [ ] Statistics align with related cases in same jurisdiction
- [ ] No contradictory claims within same document
- [ ] Proper use of estimation markers when uncertainty exists
- [ ] Clear distinction between different metrics (rates, totals, etc.)

---

## 🎓 Training Resources

### **Required Reading for Contributors:**
1. **Reality Reasoner 3.0 Protocol**: Foundation for all verification
2. **Statistics Literacy Guide**: Understanding confidence intervals, sampling error
3. **Government Data Navigation**: How to find and verify official statistics
4. **Academic Source Evaluation**: Assessing quality of research studies

### **Certification Process:**
New contributors handling statistical data must:
1. Pass verification quiz with 90%+ score
2. Successfully verify 3 existing cases
3. Submit 1 new case that passes peer review
4. Commit to quarterly update responsibilities

---

## 🚨 Emergency Correction Protocol

When incorrect data is discovered:

### **Severity Levels:**

**🔴 CRITICAL (Immediate Action Required)**
- Major statistical errors (>10% deviation from correct value)  
- Broken fundamental claims about legal compliance
- **Action**: Stop all promotion, correct within 4 hours

**🟡 IMPORTANT (24-hour Response)**
- Minor statistical corrections (<10% deviation)
- Source link updates or clarifications
- **Action**: Update data, document changes

**🟢 ROUTINE (Weekly Updates)**
- Metadata improvements  
- Additional sources for cross-validation
- **Action**: Include in regular update cycle

### **Communication Protocol:**
1. **Internal**: Immediate notification to all contributors
2. **External**: Update website/README within timeframe
3. **Academic**: Notify any citing papers if changes are significant
4. **Community**: Post in GitHub Discussions for transparency

---

## 📊 Success Metrics

**Data Quality KPIs:**
- **Verification Rate**: >95% of statistics have official sources
- **Update Frequency**: Quarterly updates completed on schedule  
- **Error Rate**: <1% of statistics require correction per year
- **Source Availability**: >99% of cited sources remain accessible

**Review this protocol quarterly and update based on lessons learned.**

---

*"Trust but verify" - LegalGapDB Data Quality Motto*