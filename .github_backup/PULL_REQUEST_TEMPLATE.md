# Pull Request

## 📝 Description
<!-- Provide a clear and concise description of your changes -->

## 🎯 Type of Change
<!-- Mark the type of change with [x] -->
- [ ] 🆕 New case submission
- [ ] 🔧 Bug fix
- [ ] ✨ New feature
- [ ] 📚 Documentation update
- [ ] 🔍 Data validation/correction
- [ ] 🎨 Website/UI improvement
- [ ] 🤖 Automation/workflow update
- [ ] 🧹 Code cleanup/refactoring

## 📊 Case Information (if applicable)
<!-- Fill this section if you're adding new cases -->

**Cases Added:**
- Jurisdiction: 
- Legal Area: 
- Case IDs: 

**Data Sources:**
<!-- List the primary sources used for case data -->
- [ ] Official government sources
- [ ] Academic research
- [ ] Legal databases
- [ ] News reports
- [ ] Other: 

## ✅ Validation Checklist
<!-- Mark completed items with [x] -->

### General Requirements
- [ ] All new files follow the project naming conventions
- [ ] Changes are within scope of LegalGapDB's mission
- [ ] No sensitive or confidential information included

### For New Cases
- [ ] JSON files pass schema validation (`python tools/validate_case.py`)
- [ ] Case IDs follow the format: `{COUNTRY}-{AREA}-{NUMBER}`
- [ ] All required fields are populated
- [ ] Citations include accessible URLs where possible
- [ ] Gap analysis clearly distinguishes formal vs. informal practices
- [ ] Sources are credible and verifiable

### For Code Changes
- [ ] Code follows existing style conventions
- [ ] New dependencies are justified and documented
- [ ] Changes don't break existing functionality
- [ ] Documentation updated if needed

### For Documentation Changes
- [ ] Content is accurate and up-to-date
- [ ] Links work correctly
- [ ] Language is clear and accessible
- [ ] Follows project voice and tone

## 🧪 Testing
<!-- Describe how you tested your changes -->

**Validation Results:**
```
# Paste output from validation tools here
```

**Manual Testing:**
<!-- Describe any manual testing performed -->

## 📸 Screenshots (if applicable)
<!-- Add screenshots for UI/website changes -->

## 🔗 Related Issues
<!-- Link to related issues using: Closes #123, Fixes #456, Related to #789 -->

## 🤝 Collaboration
<!-- If this work builds on someone else's contribution, acknowledge them -->

## 📋 Additional Notes
<!-- Any additional context, concerns, or questions for reviewers -->

## 📚 For Reviewers
<!-- Guidelines for those reviewing this PR -->

**Review Focus Areas:**
- [ ] Data accuracy and completeness
- [ ] Citation quality and accessibility  
- [ ] JSON schema compliance
- [ ] Documentation clarity
- [ ] Code quality (if applicable)

**Testing Instructions:**
<!-- Specific steps for reviewers to test changes -->

---

## 🏆 Contributor Acknowledgment
By submitting this PR, I confirm that:
- [ ] I have read and followed the [Contributing Guidelines](CONTRIBUTING.md)
- [ ] I agree to the project's dual licensing terms
- [ ] My contributions are original or properly attributed
- [ ] I understand this work will help build Legal AI for 88% of humanity

**Thank you for contributing to LegalGapDB! 🌍⚖️**