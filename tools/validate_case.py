#!/usr/bin/env python3
"""
LegalGapDB Case Validator

This script validates legal gap case JSON files against the schema and performs
additional checks including citation accessibility, data consistency, and completeness.

Usage:
    python validate_case.py <case_file.json>
    python validate_case.py --batch cases/AR/labor/
    python validate_case.py --all
"""

import json
import sys
import re
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import click
from jsonschema import validate, ValidationError, Draft7Validator

# Configuration
SCHEMA_PATH = Path(__file__).parent.parent / "validation" / "validation_schema.json"
TIMEOUT_SECONDS = 10
USER_AGENT = "LegalGapDB-Validator/1.0 (https://github.com/adrianlerer/LegalGapDB)"

class CaseValidator:
    """Validates LegalGapDB case files against schema and business rules."""
    
    def __init__(self, schema_path: Path = SCHEMA_PATH):
        """Initialize validator with schema."""
        try:
            with open(schema_path, 'r', encoding='utf-8') as f:
                self.schema = json.load(f)
            self.validator = Draft7Validator(self.schema)
        except FileNotFoundError:
            click.echo(f"❌ Schema file not found: {schema_path}", err=True)
            sys.exit(1)
        except json.JSONDecodeError as e:
            click.echo(f"❌ Invalid JSON in schema: {e}", err=True)
            sys.exit(1)
    
    def validate_case(self, case_path: Path) -> Tuple[bool, List[str]]:
        """
        Validate a single case file.
        
        Returns:
            Tuple of (success: bool, errors: List[str])
        """
        errors = []
        
        try:
            # Load case file
            with open(case_path, 'r', encoding='utf-8') as f:
                case_data = json.load(f)
        except FileNotFoundError:
            return False, [f"File not found: {case_path}"]
        except json.JSONDecodeError as e:
            return False, [f"Invalid JSON: {e}"]
        
        # Schema validation
        schema_errors = self._validate_schema(case_data)
        errors.extend(schema_errors)
        
        # Business rule validation
        business_errors = self._validate_business_rules(case_data, case_path)
        errors.extend(business_errors)
        
        # Citation validation (non-blocking)
        citation_warnings = self._validate_citations(case_data)
        if citation_warnings:
            errors.extend([f"⚠️  {w}" for w in citation_warnings])
        
        return len([e for e in errors if not e.startswith("⚠️")]) == 0, errors
    
    def _validate_schema(self, case_data: Dict) -> List[str]:
        """Validate case against JSON schema."""
        errors = []
        
        try:
            validate(instance=case_data, schema=self.schema)
        except ValidationError as e:
            errors.append(f"Schema validation failed: {e.message}")
            if e.path:
                errors.append(f"  Path: {' -> '.join(str(p) for p in e.path)}")
        
        return errors
    
    def _validate_business_rules(self, case_data: Dict, case_path: Path) -> List[str]:
        """Validate business rules and data consistency."""
        errors = []
        
        # File naming consistency
        case_id = case_data.get('case_id', '')
        expected_filename = f"{case_id}.json"
        if case_path.name != expected_filename:
            errors.append(f"File name '{case_path.name}' doesn't match case_id '{case_id}' (expected: {expected_filename})")
        
        # Case ID consistency in metadata
        metadata_case_id = case_data.get('metadata', {}).get('case_id', '')
        if case_id != metadata_case_id:
            errors.append(f"case_id mismatch: main='{case_id}', metadata='{metadata_case_id}'")
        
        # Case ID format validation
        if not re.match(r'^[A-Z]{2}-[A-Z]+[A-Z0-9]*-[0-9]{3}$', case_id):
            errors.append(f"Invalid case_id format: '{case_id}' (expected: XX-DOMAIN-NNN)")
        
        # Date consistency
        date_contributed = case_data.get('metadata', {}).get('date_contributed')
        date_updated = case_data.get('metadata', {}).get('date_last_updated')
        
        if date_contributed and date_updated:
            try:
                contrib_date = datetime.strptime(date_contributed, '%Y-%m-%d')
                update_date = datetime.strptime(date_updated, '%Y-%m-%d')
                if update_date < contrib_date:
                    errors.append(f"date_last_updated ({date_updated}) is before date_contributed ({date_contributed})")
            except ValueError as e:
                errors.append(f"Invalid date format: {e}")
        
        # Data year validation
        data_year = case_data.get('informal_practice', {}).get('gap_quantification', {}).get('data_year')
        current_year = datetime.now().year
        if data_year and (data_year < 2000 or data_year > current_year + 1):
            errors.append(f"Suspicious data_year: {data_year} (should be 2000-{current_year + 1})")
        
        # Quantification consistency
        gap_quant = case_data.get('informal_practice', {}).get('gap_quantification', {})
        value = gap_quant.get('value')
        unit = gap_quant.get('unit', '').lower()
        
        if value is not None and unit == 'percent':
            if value < 0 or value > 100:
                errors.append(f"Invalid percentage value: {value}% (should be 0-100)")
        
        # Language consistency
        languages = case_data.get('metadata', {}).get('languages', [])
        formal_lang = case_data.get('formal_rule', {}).get('language')
        
        if formal_lang and formal_lang not in languages:
            errors.append(f"formal_rule language '{formal_lang}' not listed in metadata languages {languages}")
        
        # English abstract required
        if 'en' not in languages:
            errors.append("English ('en') must be included in metadata.languages (english_abstract is required)")
        
        # Related cases format
        related_cases = case_data.get('metadata', {}).get('related_cases', [])
        for related_id in related_cases:
            if not re.match(r'^[A-Z]{2}-[A-Z]+[A-Z0-9]*-[0-9]{3}$', related_id):
                errors.append(f"Invalid related case ID format: '{related_id}'")
        
        return errors
    
    def _validate_citations(self, case_data: Dict) -> List[str]:
        """Validate that citations are accessible (non-blocking)."""
        warnings = []
        
        # Check formal rule citation
        formal_citation = case_data.get('formal_rule', {}).get('citation')
        if formal_citation:
            accessible, msg = self._check_url_accessible(formal_citation)
            if not accessible:
                warnings.append(f"formal_rule citation inaccessible: {formal_citation} ({msg})")
        
        # Check informal practice citations
        informal_citations = case_data.get('informal_practice', {}).get('citations', [])
        for i, citation in enumerate(informal_citations):
            accessible, msg = self._check_url_accessible(citation)
            if not accessible:
                warnings.append(f"informal_practice citation {i+1} inaccessible: {citation} ({msg})")
        
        return warnings
    
    def _check_url_accessible(self, url: str) -> Tuple[bool, str]:
        """Check if URL is accessible."""
        try:
            response = requests.head(
                url, 
                timeout=TIMEOUT_SECONDS,
                allow_redirects=True,
                headers={'User-Agent': USER_AGENT}
            )
            if response.status_code == 200:
                return True, "OK"
            elif 200 <= response.status_code < 400:
                return True, f"HTTP {response.status_code}"
            else:
                return False, f"HTTP {response.status_code}"
        except requests.exceptions.Timeout:
            return False, "Timeout"
        except requests.exceptions.ConnectionError:
            return False, "Connection failed"
        except requests.exceptions.RequestException as e:
            return False, str(e)
        except Exception as e:
            return False, f"Unexpected error: {e}"


def find_case_files(path: Path) -> List[Path]:
    """Find all JSON case files in a directory or return single file."""
    if path.is_file():
        if path.suffix.lower() == '.json':
            return [path]
        else:
            click.echo(f"❌ Not a JSON file: {path}", err=True)
            return []
    elif path.is_dir():
        return list(path.rglob('*.json'))
    else:
        click.echo(f"❌ Path not found: {path}", err=True)
        return []


@click.command()
@click.argument('path', required=False, type=click.Path(exists=True, path_type=Path))
@click.option('--batch', is_flag=True, help='Validate all JSON files in directory')
@click.option('--all', is_flag=True, help='Validate all cases in repository')
@click.option('--quiet', '-q', is_flag=True, help='Only show errors, not success messages')
@click.option('--no-citations', is_flag=True, help='Skip citation accessibility checks')
def main(path: Optional[Path], batch: bool, all: bool, quiet: bool, no_citations: bool):
    """
    Validate LegalGapDB case files.
    
    Examples:
        python validate_case.py cases/AR/labor/AR-LAB-001.json
        python validate_case.py --batch cases/AR/labor/
        python validate_case.py --all
    """
    validator = CaseValidator()
    
    # Determine which files to validate
    if all:
        cases_dir = Path(__file__).parent.parent / "cases"
        case_files = find_case_files(cases_dir)
    elif path:
        case_files = find_case_files(path)
    else:
        click.echo("❌ Please provide a path, use --batch, or --all", err=True)
        sys.exit(1)
    
    if not case_files:
        click.echo("❌ No JSON case files found", err=True)
        sys.exit(1)
    
    # Validate files
    total_files = len(case_files)
    successful = 0
    failed = 0
    
    click.echo(f"🔍 Validating {total_files} case file(s)...")
    click.echo()
    
    for case_file in sorted(case_files):
        success, errors = validator.validate_case(case_file)
        
        if success:
            successful += 1
            if not quiet:
                click.echo(f"✅ {case_file.name}: PASSED")
        else:
            failed += 1
            click.echo(f"❌ {case_file.name}: FAILED")
            for error in errors:
                click.echo(f"   {error}")
        
        # Show warnings even for successful cases
        warnings = [e for e in errors if e.startswith("⚠️")]
        if warnings and not quiet:
            for warning in warnings:
                click.echo(f"   {warning}")
    
    # Summary
    click.echo()
    click.echo(f"📊 Validation Summary:")
    click.echo(f"   ✅ Passed: {successful}")
    click.echo(f"   ❌ Failed: {failed}")
    click.echo(f"   📁 Total: {total_files}")
    
    if failed > 0:
        click.echo(f"\n💡 Fix the errors above and run validation again.")
        sys.exit(1)
    else:
        if not quiet:
            click.echo(f"\n🎉 All cases validated successfully!")


if __name__ == '__main__':
    main()