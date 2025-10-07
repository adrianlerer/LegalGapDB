#!/usr/bin/env python3
"""
LegalGapDB Corpus Exporter

Export legal gap cases in various formats for machine learning and analysis.
Supports JSON Lines, CSV, Excel, and training-optimized formats.

Usage:
    python export_corpus.py --format jsonl --output corpus.jsonl
    python export_corpus.py --format csv --include-metadata --output analysis.csv
    python export_corpus.py --format excel --filter-country AR --output argentina.xlsx
"""

import json
import csv
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import click
import pandas as pd

class CorpusExporter:
    """Export LegalGapDB cases in various formats."""
    
    def __init__(self, cases_dir: Path = None):
        """Initialize exporter with cases directory."""
        if cases_dir is None:
            cases_dir = Path(__file__).parent.parent / "cases"
        self.cases_dir = cases_dir
        self.cases = []
    
    def load_cases(self, 
                   country_filter: Optional[str] = None,
                   domain_filter: Optional[str] = None,
                   status_filter: Optional[str] = None) -> int:
        """
        Load cases from filesystem with optional filters.
        
        Args:
            country_filter: Two-letter country code (e.g., 'AR')
            domain_filter: Legal domain (e.g., 'Labor Law')
            status_filter: Validation status (e.g., 'verified')
            
        Returns:
            Number of cases loaded
        """
        self.cases = []
        
        # Find all JSON files in cases directory
        json_files = list(self.cases_dir.rglob('*.json'))
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    case_data = json.load(f)
                
                # Apply filters
                if country_filter:
                    case_country = case_data.get('case_id', '').split('-')[0]
                    if case_country != country_filter.upper():
                        continue
                
                if domain_filter:
                    if case_data.get('legal_domain') != domain_filter:
                        continue
                
                if status_filter:
                    metadata_status = case_data.get('metadata', {}).get('validation_status')
                    if metadata_status != status_filter:
                        continue
                
                # Add file path for reference
                case_data['_file_path'] = str(json_file.relative_to(self.cases_dir))
                self.cases.append(case_data)
                
            except (json.JSONDecodeError, KeyError) as e:
                click.echo(f"⚠️  Skipping invalid case file {json_file}: {e}", err=True)
                continue
        
        return len(self.cases)
    
    def export_jsonl(self, output_path: Path, include_metadata: bool = True) -> None:
        """Export as JSON Lines format (one JSON object per line)."""
        with open(output_path, 'w', encoding='utf-8') as f:
            for case in self.cases:
                # Optionally strip metadata
                if not include_metadata:
                    case_copy = case.copy()
                    case_copy.pop('metadata', None)
                    case_copy.pop('_file_path', None)
                    f.write(json.dumps(case_copy, ensure_ascii=False) + '\n')
                else:
                    f.write(json.dumps(case, ensure_ascii=False) + '\n')
    
    def export_csv(self, output_path: Path, include_metadata: bool = True) -> None:
        """Export as CSV with flattened structure."""
        if not self.cases:
            click.echo("❌ No cases to export", err=True)
            return
        
        # Flatten case data
        flattened_cases = []
        for case in self.cases:
            flat_case = self._flatten_case(case, include_metadata)
            flattened_cases.append(flat_case)
        
        # Convert to DataFrame and export
        df = pd.DataFrame(flattened_cases)
        df.to_csv(output_path, index=False, encoding='utf-8')
    
    def export_excel(self, output_path: Path, include_metadata: bool = True) -> None:
        """Export as Excel with multiple sheets."""
        if not self.cases:
            click.echo("❌ No cases to export", err=True)
            return
        
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Main data sheet
            flattened_cases = []
            for case in self.cases:
                flat_case = self._flatten_case(case, include_metadata)
                flattened_cases.append(flat_case)
            
            df_main = pd.DataFrame(flattened_cases)
            df_main.to_excel(writer, sheet_name='Cases', index=False)
            
            # Summary statistics sheet
            df_summary = self._generate_summary_stats()
            df_summary.to_excel(writer, sheet_name='Summary', index=False)
            
            # Domain breakdown sheet
            df_domains = self._generate_domain_breakdown()
            df_domains.to_excel(writer, sheet_name='Domains', index=False)
    
    def export_training_format(self, output_path: Path, format_type: str = 'classification') -> None:
        """
        Export in ML training-optimized format.
        
        Args:
            format_type: 'classification', 'regression', or 'text_generation'
        """
        if format_type == 'classification':
            self._export_classification_format(output_path)
        elif format_type == 'regression':
            self._export_regression_format(output_path)
        elif format_type == 'text_generation':
            self._export_text_generation_format(output_path)
        else:
            click.echo(f"❌ Unknown format type: {format_type}", err=True)
    
    def _flatten_case(self, case: Dict, include_metadata: bool) -> Dict[str, Any]:
        """Flatten nested case structure for tabular export."""
        flat = {}
        
        # Basic fields
        flat['case_id'] = case.get('case_id', '')
        flat['title'] = case.get('title', '')
        flat['jurisdiction'] = case.get('jurisdiction', '')
        flat['legal_domain'] = case.get('legal_domain', '')
        flat['sub_domain'] = case.get('sub_domain', '')
        
        # Formal rule
        formal_rule = case.get('formal_rule', {})
        flat['formal_rule_text'] = formal_rule.get('text', '')
        flat['formal_rule_source'] = formal_rule.get('source', '')
        flat['formal_rule_citation'] = formal_rule.get('citation', '')
        flat['formal_rule_language'] = formal_rule.get('language', '')
        flat['date_enacted'] = formal_rule.get('date_enacted', '')
        
        # Informal practice
        informal_practice = case.get('informal_practice', {})
        flat['informal_practice_text'] = informal_practice.get('text', '')
        
        # Gap quantification
        gap_quant = informal_practice.get('gap_quantification', {})
        flat['gap_metric'] = gap_quant.get('metric', '')
        flat['gap_value'] = gap_quant.get('value', 0)
        flat['gap_unit'] = gap_quant.get('unit', '')
        flat['gap_confidence'] = gap_quant.get('confidence', '')
        flat['data_year'] = gap_quant.get('data_year', '')
        flat['absolute_number'] = gap_quant.get('absolute_number', 0)
        
        # Gap mechanism
        gap_mechanism = case.get('gap_mechanism', {})
        flat['gap_mechanism_text'] = gap_mechanism.get('text', '')
        flat['mechanism_types'] = ', '.join(gap_mechanism.get('mechanism_types', []))
        
        # Outcome data
        outcome_data = case.get('outcome_data', {})
        flat['probability_detection'] = outcome_data.get('probability_of_detection', 0)
        flat['probability_penalty'] = outcome_data.get('probability_of_penalty_if_detected', 0)
        flat['voluntary_compliance'] = outcome_data.get('voluntary_compliance_rate', 0)
        flat['actual_compliance'] = outcome_data.get('actual_compliance_including_enforcement', 0)
        
        # English abstract
        english_abstract = case.get('english_abstract', {})
        flat['abstract_formal'] = english_abstract.get('formal', '')
        flat['abstract_informal'] = english_abstract.get('informal', '')
        flat['abstract_gap'] = english_abstract.get('gap', '')
        
        # Metadata (optional)
        if include_metadata:
            metadata = case.get('metadata', {})
            flat['contributor'] = metadata.get('contributor', '')
            flat['date_contributed'] = metadata.get('date_contributed', '')
            flat['validation_status'] = metadata.get('validation_status', '')
            flat['version'] = metadata.get('version', '')
            flat['languages'] = ', '.join(metadata.get('languages', []))
            flat['tags'] = ', '.join(metadata.get('tags', []))
            flat['file_path'] = case.get('_file_path', '')
        
        return flat
    
    def _generate_summary_stats(self) -> pd.DataFrame:
        """Generate summary statistics DataFrame."""
        stats = []
        
        # Overall stats
        stats.append({'Metric': 'Total Cases', 'Value': len(self.cases)})
        
        # Country breakdown
        countries = {}
        for case in self.cases:
            country = case.get('case_id', '').split('-')[0]
            countries[country] = countries.get(country, 0) + 1
        
        for country, count in sorted(countries.items()):
            stats.append({'Metric': f'Cases - {country}', 'Value': count})
        
        # Domain breakdown
        domains = {}
        for case in self.cases:
            domain = case.get('legal_domain', 'Unknown')
            domains[domain] = domains.get(domain, 0) + 1
        
        for domain, count in sorted(domains.items()):
            stats.append({'Metric': f'Domain - {domain}', 'Value': count})
        
        # Validation status
        statuses = {}
        for case in self.cases:
            status = case.get('metadata', {}).get('validation_status', 'unknown')
            statuses[status] = statuses.get(status, 0) + 1
        
        for status, count in sorted(statuses.items()):
            stats.append({'Metric': f'Status - {status}', 'Value': count})
        
        return pd.DataFrame(stats)
    
    def _generate_domain_breakdown(self) -> pd.DataFrame:
        """Generate domain-specific breakdown."""
        domains_data = []
        
        for case in self.cases:
            domain_info = {
                'case_id': case.get('case_id', ''),
                'jurisdiction': case.get('jurisdiction', ''),
                'legal_domain': case.get('legal_domain', ''),
                'sub_domain': case.get('sub_domain', ''),
                'gap_value': case.get('informal_practice', {}).get('gap_quantification', {}).get('value', 0),
                'gap_unit': case.get('informal_practice', {}).get('gap_quantification', {}).get('unit', ''),
                'confidence': case.get('informal_practice', {}).get('gap_quantification', {}).get('confidence', ''),
                'mechanisms': ', '.join(case.get('gap_mechanism', {}).get('mechanism_types', [])),
                'validation_status': case.get('metadata', {}).get('validation_status', '')
            }
            domains_data.append(domain_info)
        
        return pd.DataFrame(domains_data)
    
    def _export_classification_format(self, output_path: Path) -> None:
        """Export for classification tasks (predict compliance level)."""
        training_data = []
        
        for case in self.cases:
            # Features
            features = {
                'jurisdiction': case.get('jurisdiction', ''),
                'legal_domain': case.get('legal_domain', ''),
                'mechanism_types': case.get('gap_mechanism', {}).get('mechanism_types', []),
                'formal_rule_text': case.get('formal_rule', {}).get('text', ''),
                'gap_mechanism_text': case.get('gap_mechanism', {}).get('text', ''),
            }
            
            # Target (compliance level)
            compliance_rate = case.get('outcome_data', {}).get('voluntary_compliance_rate', 0)
            if compliance_rate >= 80:
                label = 'high_compliance'
            elif compliance_rate >= 50:
                label = 'medium_compliance'
            else:
                label = 'low_compliance'
            
            training_data.append({
                'case_id': case.get('case_id', ''),
                'features': features,
                'label': label,
                'compliance_rate': compliance_rate
            })
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in training_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    def _export_regression_format(self, output_path: Path) -> None:
        """Export for regression tasks (predict exact compliance rate)."""
        training_data = []
        
        for case in self.cases:
            # Features
            gap_quant = case.get('informal_practice', {}).get('gap_quantification', {})
            outcome = case.get('outcome_data', {})
            
            features = {
                'jurisdiction': case.get('jurisdiction', ''),
                'legal_domain': case.get('legal_domain', ''),
                'mechanism_types': case.get('gap_mechanism', {}).get('mechanism_types', []),
                'data_year': gap_quant.get('data_year', 2024),
                'probability_detection': outcome.get('probability_of_detection', 0),
                'probability_penalty': outcome.get('probability_of_penalty_if_detected', 0),
            }
            
            # Target
            target = outcome.get('voluntary_compliance_rate', 0)
            
            training_data.append({
                'case_id': case.get('case_id', ''),
                'features': features,
                'target': target
            })
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in training_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    def _export_text_generation_format(self, output_path: Path) -> None:
        """Export for text generation tasks (generate gap explanations)."""
        training_data = []
        
        for case in self.cases:
            # Input context
            context = f"Country: {case.get('jurisdiction', '')}\n"
            context += f"Legal Domain: {case.get('legal_domain', '')}\n"
            context += f"Formal Rule: {case.get('english_abstract', {}).get('formal', '')}\n"
            context += f"Informal Practice: {case.get('english_abstract', {}).get('informal', '')}\n"
            
            # Target (gap explanation)
            target = case.get('english_abstract', {}).get('gap', '')
            
            training_data.append({
                'case_id': case.get('case_id', ''),
                'context': context,
                'target': target
            })
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in training_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')


@click.command()
@click.option('--format', 'export_format', 
              type=click.Choice(['json', 'jsonl', 'csv', 'excel', 'ml-classification', 'ml-regression', 'ml-text']),
              default='jsonl',
              help='Export format')
@click.option('--output', '-o', 
              type=click.Path(path_type=Path),
              required=True,
              help='Output file path')
@click.option('--filter-country', 
              help='Filter by country code (e.g., AR, BR)')
@click.option('--filter-domain',
              help='Filter by legal domain (e.g., "Labor Law")')
@click.option('--filter-status',
              help='Filter by validation status (e.g., verified, seed_case)')
@click.option('--include-metadata/--no-metadata',
              default=True,
              help='Include metadata fields in export')
@click.option('--cases-dir',
              type=click.Path(exists=True, file_okay=False, path_type=Path),
              help='Custom cases directory path')
def main(export_format: str, 
         output: Path,
         filter_country: Optional[str],
         filter_domain: Optional[str], 
         filter_status: Optional[str],
         include_metadata: bool,
         cases_dir: Optional[Path]):
    """
    Export LegalGapDB cases in various formats.
    
    Examples:
        # Export all cases as JSON Lines
        python export_corpus.py --format jsonl --output corpus.jsonl
        
        # Export Argentina cases as CSV
        python export_corpus.py --format csv --filter-country AR --output argentina.csv
        
        # Export for ML classification task
        python export_corpus.py --format ml-classification --output training.jsonl
    """
    
    # Initialize exporter
    exporter = CorpusExporter(cases_dir)
    
    # Load cases with filters
    click.echo("🔍 Loading cases...")
    num_cases = exporter.load_cases(
        country_filter=filter_country,
        domain_filter=filter_domain,
        status_filter=filter_status
    )
    
    if num_cases == 0:
        click.echo("❌ No cases found matching the specified filters", err=True)
        sys.exit(1)
    
    click.echo(f"✅ Loaded {num_cases} cases")
    
    # Export in specified format
    click.echo(f"📤 Exporting to {export_format} format...")
    
    try:
        if export_format == 'json':
            with open(output, 'w', encoding='utf-8') as f:
                json.dump(exporter.cases, f, ensure_ascii=False, indent=2)
        
        elif export_format == 'jsonl':
            exporter.export_jsonl(output, include_metadata)
        
        elif export_format == 'csv':
            exporter.export_csv(output, include_metadata)
        
        elif export_format == 'excel':
            exporter.export_excel(output, include_metadata)
        
        elif export_format == 'ml-classification':
            exporter.export_training_format(output, 'classification')
        
        elif export_format == 'ml-regression':
            exporter.export_training_format(output, 'regression')
        
        elif export_format == 'ml-text':
            exporter.export_training_format(output, 'text_generation')
        
        click.echo(f"✅ Export completed: {output}")
        click.echo(f"📊 Exported {num_cases} cases")
        
    except Exception as e:
        click.echo(f"❌ Export failed: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()