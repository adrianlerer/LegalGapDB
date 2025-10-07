#!/usr/bin/env python3
"""
LegalGapDB Statistics Dashboard

Generate statistical analysis and visualizations of the legal gaps database.

Usage:
    python stats_dashboard.py --output stats_report.html
    python stats_dashboard.py --format json --output stats.json
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from collections import Counter, defaultdict
import click

class StatsDashboard:
    """Generate statistics and analysis for LegalGapDB."""
    
    def __init__(self, cases_dir: Path = None):
        """Initialize dashboard with cases directory."""
        if cases_dir is None:
            cases_dir = Path(__file__).parent.parent / "cases"
        self.cases_dir = cases_dir
        self.cases = []
        self.stats = {}
    
    def load_cases(self) -> int:
        """Load all valid cases from filesystem."""
        self.cases = []
        
        json_files = list(self.cases_dir.rglob('*.json'))
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    case_data = json.load(f)
                
                # Basic validation
                if 'case_id' in case_data and 'legal_domain' in case_data:
                    case_data['_file_path'] = str(json_file.relative_to(self.cases_dir))
                    self.cases.append(case_data)
                    
            except (json.JSONDecodeError, KeyError):
                continue
        
        return len(self.cases)
    
    def generate_stats(self) -> Dict[str, Any]:
        """Generate comprehensive statistics."""
        self.stats = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_cases': len(self.cases),
                'version': '1.0'
            },
            'overview': self._generate_overview_stats(),
            'geographic': self._generate_geographic_stats(),
            'domains': self._generate_domain_stats(),
            'gaps': self._generate_gap_stats(),
            'mechanisms': self._generate_mechanism_stats(),
            'compliance': self._generate_compliance_stats(),
            'temporal': self._generate_temporal_stats(),
            'quality': self._generate_quality_stats()
        }
        
        return self.stats
    
    def _generate_overview_stats(self) -> Dict[str, Any]:
        """Generate overview statistics."""
        countries = set()
        domains = set()
        languages = set()
        
        for case in self.cases:
            # Extract country from case_id
            country = case.get('case_id', '').split('-')[0]
            if country:
                countries.add(country)
            
            # Legal domain
            domain = case.get('legal_domain')
            if domain:
                domains.add(domain)
            
            # Languages
            case_languages = case.get('metadata', {}).get('languages', [])
            languages.update(case_languages)
        
        return {
            'total_cases': len(self.cases),
            'countries_count': len(countries),
            'countries': sorted(list(countries)),
            'legal_domains_count': len(domains),
            'legal_domains': sorted(list(domains)),
            'languages_count': len(languages),
            'languages': sorted(list(languages))
        }
    
    def _generate_geographic_stats(self) -> Dict[str, Any]:
        """Generate geographic distribution statistics."""
        country_stats = Counter()
        country_domains = defaultdict(set)
        
        for case in self.cases:
            country = case.get('case_id', '').split('-')[0]
            domain = case.get('legal_domain', '')
            
            if country:
                country_stats[country] += 1
                if domain:
                    country_domains[country].add(domain)
        
        # Convert sets to lists for JSON serialization
        country_domains_dict = {
            country: sorted(list(domains)) 
            for country, domains in country_domains.items()
        }
        
        return {
            'by_country': dict(country_stats.most_common()),
            'domains_by_country': country_domains_dict,
            'country_rankings': [
                {'country': country, 'cases': count, 'rank': i+1}
                for i, (country, count) in enumerate(country_stats.most_common())
            ]
        }
    
    def _generate_domain_stats(self) -> Dict[str, Any]:
        """Generate legal domain statistics."""
        domain_stats = Counter()
        subdomain_stats = Counter()
        domain_countries = defaultdict(set)
        
        for case in self.cases:
            domain = case.get('legal_domain', '')
            subdomain = case.get('sub_domain', '')
            country = case.get('case_id', '').split('-')[0]
            
            if domain:
                domain_stats[domain] += 1
                if country:
                    domain_countries[domain].add(country)
            
            if subdomain:
                subdomain_stats[subdomain] += 1
        
        # Convert sets to lists
        domain_countries_dict = {
            domain: sorted(list(countries))
            for domain, countries in domain_countries.items()
        }
        
        return {
            'by_domain': dict(domain_stats.most_common()),
            'by_subdomain': dict(subdomain_stats.most_common(10)),  # Top 10
            'countries_by_domain': domain_countries_dict,
            'domain_rankings': [
                {'domain': domain, 'cases': count, 'rank': i+1}
                for i, (domain, count) in enumerate(domain_stats.most_common())
            ]
        }
    
    def _generate_gap_stats(self) -> Dict[str, Any]:
        """Generate gap quantification statistics."""
        gap_values = []
        confidence_levels = Counter()
        units = Counter()
        
        for case in self.cases:
            gap_quant = case.get('informal_practice', {}).get('gap_quantification', {})
            
            value = gap_quant.get('value')
            if value is not None:
                gap_values.append(value)
            
            confidence = gap_quant.get('confidence')
            if confidence:
                confidence_levels[confidence] += 1
            
            unit = gap_quant.get('unit')
            if unit:
                units[unit] += 1
        
        # Calculate statistics for gap values
        gap_stats = {}
        if gap_values:
            gap_stats = {
                'min': min(gap_values),
                'max': max(gap_values),
                'mean': sum(gap_values) / len(gap_values),
                'median': sorted(gap_values)[len(gap_values) // 2],
                'count': len(gap_values)
            }
        
        return {
            'gap_value_stats': gap_stats,
            'confidence_distribution': dict(confidence_levels),
            'unit_distribution': dict(units),
            'high_gap_cases': [
                case.get('case_id', '')
                for case in self.cases
                if case.get('informal_practice', {}).get('gap_quantification', {}).get('value', 0) > 50
            ]
        }
    
    def _generate_mechanism_stats(self) -> Dict[str, Any]:
        """Generate gap mechanism statistics."""
        mechanism_counts = Counter()
        mechanism_combinations = Counter()
        
        for case in self.cases:
            mechanisms = case.get('gap_mechanism', {}).get('mechanism_types', [])
            
            # Count individual mechanisms
            for mechanism in mechanisms:
                mechanism_counts[mechanism] += 1
            
            # Count mechanism combinations
            if len(mechanisms) > 1:
                combo = tuple(sorted(mechanisms))
                mechanism_combinations[combo] += 1
        
        return {
            'mechanism_frequency': dict(mechanism_counts.most_common()),
            'common_combinations': [
                {'mechanisms': list(combo), 'count': count}
                for combo, count in mechanism_combinations.most_common(5)
            ],
            'mechanism_rankings': [
                {'mechanism': mech, 'cases': count, 'percentage': round(count/len(self.cases)*100, 1)}
                for mech, count in mechanism_counts.most_common()
            ]
        }
    
    def _generate_compliance_stats(self) -> Dict[str, Any]:
        """Generate compliance rate statistics."""
        voluntary_rates = []
        actual_rates = []
        detection_probs = []
        
        for case in self.cases:
            outcome = case.get('outcome_data', {})
            
            vol_rate = outcome.get('voluntary_compliance_rate')
            if vol_rate is not None:
                voluntary_rates.append(vol_rate)
            
            actual_rate = outcome.get('actual_compliance_including_enforcement')
            if actual_rate is not None:
                actual_rates.append(actual_rate)
            
            detection = outcome.get('probability_of_detection')
            if detection is not None:
                detection_probs.append(detection)
        
        def calc_stats(values):
            if not values:
                return {}
            return {
                'min': min(values),
                'max': max(values),
                'mean': sum(values) / len(values),
                'median': sorted(values)[len(values) // 2]
            }
        
        return {
            'voluntary_compliance': calc_stats(voluntary_rates),
            'actual_compliance': calc_stats(actual_rates),
            'detection_probability': calc_stats(detection_probs),
            'enforcement_effectiveness': {
                'cases_with_data': len([r for r in actual_rates if r is not None]),
                'average_improvement': (
                    sum(actual_rates) / len(actual_rates) - sum(voluntary_rates) / len(voluntary_rates)
                    if actual_rates and voluntary_rates else 0
                )
            }
        }
    
    def _generate_temporal_stats(self) -> Dict[str, Any]:
        """Generate temporal statistics."""
        contribution_years = Counter()
        data_years = Counter()
        
        for case in self.cases:
            # Contribution date
            contrib_date = case.get('metadata', {}).get('date_contributed')
            if contrib_date:
                try:
                    year = datetime.strptime(contrib_date, '%Y-%m-%d').year
                    contribution_years[year] += 1
                except ValueError:
                    pass
            
            # Data year
            data_year = case.get('informal_practice', {}).get('gap_quantification', {}).get('data_year')
            if data_year:
                data_years[data_year] += 1
        
        return {
            'contribution_timeline': dict(contribution_years),
            'data_coverage_years': dict(data_years),
            'data_freshness': {
                'cases_with_2024_data': data_years.get(2024, 0),
                'cases_with_2023_data': data_years.get(2023, 0),
                'oldest_data_year': min(data_years.keys()) if data_years else None,
                'newest_data_year': max(data_years.keys()) if data_years else None
            }
        }
    
    def _generate_quality_stats(self) -> Dict[str, Any]:
        """Generate data quality statistics."""
        validation_statuses = Counter()
        confidence_levels = Counter()
        citation_counts = []
        
        for case in self.cases:
            # Validation status
            status = case.get('metadata', {}).get('validation_status')
            if status:
                validation_statuses[status] += 1
            
            # Confidence level
            confidence = case.get('informal_practice', {}).get('gap_quantification', {}).get('confidence')
            if confidence:
                confidence_levels[confidence] += 1
            
            # Citation count
            citations = case.get('informal_practice', {}).get('citations', [])
            citation_counts.append(len(citations))
        
        return {
            'validation_status_distribution': dict(validation_statuses),
            'confidence_level_distribution': dict(confidence_levels),
            'citation_statistics': {
                'min_citations': min(citation_counts) if citation_counts else 0,
                'max_citations': max(citation_counts) if citation_counts else 0,
                'mean_citations': sum(citation_counts) / len(citation_counts) if citation_counts else 0,
                'cases_with_multiple_sources': len([c for c in citation_counts if c > 1])
            },
            'quality_score': {
                'high_confidence_percentage': round(confidence_levels.get('high', 0) / len(self.cases) * 100, 1),
                'verified_percentage': round(validation_statuses.get('verified', 0) / len(self.cases) * 100, 1),
                'well_sourced_percentage': round(len([c for c in citation_counts if c >= 2]) / len(self.cases) * 100, 1)
            }
        }
    
    def export_json(self, output_path: Path) -> None:
        """Export statistics as JSON."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2, ensure_ascii=False)
    
    def export_html(self, output_path: Path) -> None:
        """Export statistics as HTML report."""
        html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LegalGapDB Statistics Report</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; background: #f8f9fa; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #1a365d; border-bottom: 3px solid #3182ce; padding-bottom: 10px; }
        h2 { color: #2d3748; margin-top: 40px; }
        h3 { color: #4a5568; }
        .metric { display: inline-block; margin: 10px 20px 10px 0; padding: 15px; background: #f7fafc; border-left: 4px solid #3182ce; border-radius: 4px; }
        .metric-value { font-size: 24px; font-weight: bold; color: #1a365d; }
        .metric-label { font-size: 14px; color: #718096; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; }
        th { background: #edf2f7; font-weight: 600; }
        .progress-bar { height: 20px; background: #e2e8f0; border-radius: 10px; overflow: hidden; margin: 5px 0; }
        .progress-fill { height: 100%; background: #3182ce; transition: width 0.3s ease; }
        .footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #e2e8f0; color: #718096; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌍 LegalGapDB Statistics Report</h1>
        <p><strong>Generated:</strong> {generated_at}</p>
        
        <h2>📊 Overview</h2>
        <div class="metric">
            <div class="metric-value">{total_cases}</div>
            <div class="metric-label">Total Cases</div>
        </div>
        <div class="metric">
            <div class="metric-value">{countries_count}</div>
            <div class="metric-label">Countries</div>
        </div>
        <div class="metric">
            <div class="metric-value">{domains_count}</div>
            <div class="metric-label">Legal Domains</div>
        </div>
        <div class="metric">
            <div class="metric-value">{languages_count}</div>
            <div class="metric-label">Languages</div>
        </div>
        
        {country_section}
        {domain_section}
        {mechanism_section}
        {quality_section}
        
        <div class="footer">
            <p>This report was generated automatically by the LegalGapDB statistics tool.</p>
            <p>For more information, visit: <a href="https://github.com/adrianlerer/LegalGapDB">https://github.com/adrianlerer/LegalGapDB</a></p>
        </div>
    </div>
</body>
</html>
        """
        
        # Generate sections
        country_section = self._generate_country_html()
        domain_section = self._generate_domain_html()
        mechanism_section = self._generate_mechanism_html()
        quality_section = self._generate_quality_html()
        
        # Fill template
        html_content = html_template.format(
            generated_at=self.stats['metadata']['generated_at'],
            total_cases=self.stats['overview']['total_cases'],
            countries_count=self.stats['overview']['countries_count'],
            domains_count=self.stats['overview']['legal_domains_count'],
            languages_count=self.stats['overview']['languages_count'],
            country_section=country_section,
            domain_section=domain_section,
            mechanism_section=mechanism_section,
            quality_section=quality_section
        )
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def _generate_country_html(self) -> str:
        """Generate HTML for country statistics."""
        html = "<h2>🌎 Geographic Distribution</h2>"
        html += "<table><thead><tr><th>Country</th><th>Cases</th><th>Percentage</th><th>Distribution</th></tr></thead><tbody>"
        
        total_cases = self.stats['overview']['total_cases']
        for country_info in self.stats['geographic']['country_rankings']:
            country = country_info['country']
            cases = country_info['cases']
            percentage = round(cases / total_cases * 100, 1)
            
            html += f"<tr>"
            html += f"<td><strong>{country}</strong></td>"
            html += f"<td>{cases}</td>"
            html += f"<td>{percentage}%</td>"
            html += f'<td><div class="progress-bar"><div class="progress-fill" style="width: {percentage}%"></div></div></td>'
            html += f"</tr>"
        
        html += "</tbody></table>"
        return html
    
    def _generate_domain_html(self) -> str:
        """Generate HTML for domain statistics."""
        html = "<h2>⚖️ Legal Domains</h2>"
        html += "<table><thead><tr><th>Domain</th><th>Cases</th><th>Percentage</th><th>Distribution</th></tr></thead><tbody>"
        
        total_cases = self.stats['overview']['total_cases']
        for domain_info in self.stats['domains']['domain_rankings']:
            domain = domain_info['domain']
            cases = domain_info['cases']
            percentage = round(cases / total_cases * 100, 1)
            
            html += f"<tr>"
            html += f"<td><strong>{domain}</strong></td>"
            html += f"<td>{cases}</td>"
            html += f"<td>{percentage}%</td>"
            html += f'<td><div class="progress-bar"><div class="progress-fill" style="width: {percentage}%"></div></div></td>'
            html += f"</tr>"
        
        html += "</tbody></table>"
        return html
    
    def _generate_mechanism_html(self) -> str:
        """Generate HTML for mechanism statistics."""
        html = "<h2>🔧 Gap Mechanisms</h2>"
        html += "<table><thead><tr><th>Mechanism</th><th>Cases</th><th>Percentage</th><th>Distribution</th></tr></thead><tbody>"
        
        for mech_info in self.stats['mechanisms']['mechanism_rankings']:
            mechanism = mech_info['mechanism'].replace('_', ' ').title()
            cases = mech_info['cases']
            percentage = mech_info['percentage']
            
            html += f"<tr>"
            html += f"<td><strong>{mechanism}</strong></td>"
            html += f"<td>{cases}</td>"
            html += f"<td>{percentage}%</td>"
            html += f'<td><div class="progress-bar"><div class="progress-fill" style="width: {percentage}%"></div></div></td>'
            html += f"</tr>"
        
        html += "</tbody></table>"
        return html
    
    def _generate_quality_html(self) -> str:
        """Generate HTML for quality statistics."""
        html = "<h2>✅ Data Quality</h2>"
        
        quality_score = self.stats['quality']['quality_score']
        
        html += "<h3>Quality Indicators</h3>"
        html += f"<div class='metric'><div class='metric-value'>{quality_score['high_confidence_percentage']}%</div><div class='metric-label'>High Confidence Data</div></div>"
        html += f"<div class='metric'><div class='metric-value'>{quality_score['verified_percentage']}%</div><div class='metric-label'>Verified Cases</div></div>"
        html += f"<div class='metric'><div class='metric-value'>{quality_score['well_sourced_percentage']}%</div><div class='metric-label'>Well Sourced (2+ citations)</div></div>"
        
        return html


@click.command()
@click.option('--format', 'output_format',
              type=click.Choice(['json', 'html']),
              default='html',
              help='Output format')
@click.option('--output', '-o',
              type=click.Path(path_type=Path),
              required=True,
              help='Output file path')
@click.option('--cases-dir',
              type=click.Path(exists=True, file_okay=False, path_type=Path),
              help='Custom cases directory path')
def main(output_format: str, output: Path, cases_dir: Optional[Path]):
    """
    Generate LegalGapDB statistics report.
    
    Examples:
        python stats_dashboard.py --format html --output report.html
        python stats_dashboard.py --format json --output stats.json
    """
    
    # Initialize dashboard
    dashboard = StatsDashboard(cases_dir)
    
    # Load cases
    click.echo("🔍 Loading cases...")
    num_cases = dashboard.load_cases()
    
    if num_cases == 0:
        click.echo("❌ No cases found", err=True)
        sys.exit(1)
    
    click.echo(f"✅ Loaded {num_cases} cases")
    
    # Generate statistics
    click.echo("📊 Generating statistics...")
    dashboard.generate_stats()
    
    # Export in specified format
    click.echo(f"📤 Exporting {output_format} report...")
    
    try:
        if output_format == 'json':
            dashboard.export_json(output)
        elif output_format == 'html':
            dashboard.export_html(output)
        
        click.echo(f"✅ Report generated: {output}")
        
    except Exception as e:
        click.echo(f"❌ Export failed: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()