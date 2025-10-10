#!/usr/bin/env python3
"""
Basic validation tests for LegalGapDB

These tests ensure data integrity and prevent regression bugs.
"""

import json
import pytest
from pathlib import Path
from typing import List, Dict, Any


def get_all_case_files() -> List[Path]:
    """Get all JSON case files."""
    cases_dir = Path(__file__).parent.parent / "cases"
    return list(cases_dir.rglob("*.json"))


def load_case(case_file: Path) -> Dict[str, Any]:
    """Load a case file safely."""
    try:
        with open(case_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        pytest.fail(f"Failed to load {case_file}: {e}")


class TestDataIntegrity:
    """Test basic data integrity."""
    
    def test_all_cases_are_valid_json(self):
        """Verify all JSON files are syntactically valid."""
        case_files = get_all_case_files()
        assert len(case_files) > 0, "No case files found"
        
        for case_file in case_files:
            case_data = load_case(case_file)
            assert isinstance(case_data, dict), f"{case_file} should contain a JSON object"
    
    def test_case_count(self):
        """Verify we have exactly 19 cases in Argentina."""
        ar_cases = list((Path(__file__).parent.parent / "cases" / "AR").rglob("*.json"))
        assert len(ar_cases) == 19, f"Expected 19 Argentina cases, found {len(ar_cases)}"
    
    def test_required_fields_present(self):
        """Verify all cases have required top-level fields."""
        required_fields = [
            "case_id",
            "title", 
            "jurisdiction",
            "legal_domain",
            "formal_rule",
            "informal_practice",
            "gap_mechanism", 
            "english_abstract",
            "metadata"
        ]
        
        case_files = get_all_case_files()
        for case_file in case_files:
            case_data = load_case(case_file)
            for field in required_fields:
                assert field in case_data, f"{case_file} missing required field: {field}"
    
    def test_case_id_format(self):
        """Verify case IDs follow the correct format: XX-YYYY-###."""
        case_files = get_all_case_files()
        for case_file in case_files:
            case_data = load_case(case_file)
            case_id = case_data.get("case_id", "")
            
            # Format: AR-LAB-001, AR-TAX-002, etc.
            parts = case_id.split("-")
            assert len(parts) == 3, f"{case_file}: case_id should have format XX-YYYY-###, got {case_id}"
            
            country, domain, number = parts
            assert len(country) == 2, f"{case_file}: country code should be 2 chars, got {country}"
            assert country.isupper(), f"{case_file}: country code should be uppercase, got {country}"
            assert len(domain) >= 3, f"{case_file}: domain should be 3+ chars, got {domain}"
            assert domain.isupper(), f"{case_file}: domain should be uppercase, got {domain}"
            assert number.isdigit(), f"{case_file}: number should be digits, got {number}"
            assert len(number) == 3, f"{case_file}: number should be 3 digits, got {number}"
    
    def test_english_abstract_completeness(self):
        """Verify English abstracts have all required fields."""
        required_abstract_fields = ["formal", "informal", "gap"]
        
        case_files = get_all_case_files()
        for case_file in case_files:
            case_data = load_case(case_file)
            abstract = case_data.get("english_abstract", {})
            
            for field in required_abstract_fields:
                assert field in abstract, f"{case_file}: english_abstract missing {field}"
                assert len(abstract[field]) > 20, f"{case_file}: english_abstract.{field} too short"
    
    def test_gap_quantification_present(self):
        """Verify gap quantification data is present and reasonable."""
        case_files = get_all_case_files()
        for case_file in case_files:
            case_data = load_case(case_file)
            
            informal_practice = case_data.get("informal_practice", {})
            gap_quant = informal_practice.get("gap_quantification", {})
            
            assert "value" in gap_quant, f"{case_file}: missing gap_quantification.value"
            assert "unit" in gap_quant, f"{case_file}: missing gap_quantification.unit"
            assert "confidence" in gap_quant, f"{case_file}: missing gap_quantification.confidence"
            
            # Reasonable ranges
            value = gap_quant["value"]
            if gap_quant["unit"] == "percent":
                assert 0 <= value <= 100, f"{case_file}: percent value should be 0-100, got {value}"
    
    def test_formal_rule_citations(self):
        """Verify formal rules have proper citations."""
        case_files = get_all_case_files()
        for case_file in case_files:
            case_data = load_case(case_file)
            
            formal_rule = case_data.get("formal_rule", {})
            assert "citation" in formal_rule, f"{case_file}: missing formal_rule.citation"
            assert "source" in formal_rule, f"{case_file}: missing formal_rule.source"
            
            citation = formal_rule["citation"]
            # Should be a URL (basic check)
            assert citation.startswith(("http://", "https://")), f"{case_file}: citation should be URL"


class TestDomainCoverage:
    """Test coverage across legal domains."""
    
    def test_argentina_domain_distribution(self):
        """Verify Argentina has cases across expected domains."""
        ar_cases = list((Path(__file__).parent.parent / "cases" / "AR").rglob("*.json"))
        
        domains = []
        for case_file in ar_cases:
            case_data = load_case(case_file)
            domains.append(case_data.get("legal_domain", ""))
        
        domain_counts = {domain: domains.count(domain) for domain in set(domains)}
        
        # Should have cases in multiple domains
        assert len(domain_counts) >= 4, f"Should cover 4+ domains, got: {domain_counts}"
        
        # Expected domains based on file structure
        expected_domains = {"Labor Law", "Tax Law", "Corporate Law", "Criminal Law", "Family Law"}
        found_domains = set(domains)
        
        # Should have most expected domains
        overlap = expected_domains & found_domains
        assert len(overlap) >= 4, f"Missing expected domains. Found: {found_domains}"


class TestToolsIntegration:
    """Test that tools work with current data."""
    
    def test_export_tool_runs(self):
        """Verify export tool can process all cases without errors."""
        import subprocess
        import tempfile
        
        with tempfile.NamedTemporaryFile(suffix=".jsonl", delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            # Run export tool
            result = subprocess.run([
                "python", "tools/export_corpus.py",
                "--format", "jsonl",
                "--output", tmp_path
            ], capture_output=True, text=True, cwd=Path(__file__).parent.parent)
            
            assert result.returncode == 0, f"Export failed: {result.stderr}"
            
            # Verify output file exists and has content
            output_path = Path(tmp_path)
            assert output_path.exists(), "Export output file not created"
            assert output_path.stat().st_size > 0, "Export output file is empty"
            
            # Verify output is valid JSONL
            with open(output_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                assert len(lines) >= 19, f"Expected at least 19 lines, got {len(lines)}"
                
                # Each line should be valid JSON
                for i, line in enumerate(lines):
                    try:
                        json.loads(line.strip())
                    except json.JSONDecodeError as e:
                        pytest.fail(f"Line {i+1} is not valid JSON: {e}")
        
        finally:
            # Cleanup
            if Path(tmp_path).exists():
                Path(tmp_path).unlink()


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])