"""
Report Generation Module

This module generates formatted reports from code analysis results.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional


class ReportGenerator:
    """Generate reports from code analysis results."""

    def __init__(self, output_dir: str = "reports"):
        """
        Initialize ReportGenerator.

        Args:
            output_dir: Directory to save reports
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_text_report(self, analysis: Dict, output_file: Optional[str] = None) -> str:
        """
        Generate a text-formatted report.

        Args:
            analysis: Analysis results dictionary
            output_file: Optional file path to save report

        Returns:
            Report as string
        """
        if "error" in analysis:
            return f"Error: {analysis['error']}"

        if "directory" in analysis:
            # Directory analysis
            report = self._generate_directory_text_report(analysis)
        else:
            # Single file analysis
            report = self._generate_file_text_report(analysis)

        if output_file:
            output_path = self.output_dir / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)

        return report

    def generate_json_report(self, analysis: Dict, output_file: Optional[str] = None) -> str:
        """
        Generate a JSON-formatted report.

        Args:
            analysis: Analysis results dictionary
            output_file: Optional file path to save report

        Returns:
            Report as JSON string
        """
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "analysis": analysis
        }

        json_str = json.dumps(report_data, indent=2, ensure_ascii=False)

        if output_file:
            output_path = self.output_dir / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(json_str)

        return json_str

    def _generate_file_text_report(self, analysis: Dict) -> str:
        """Generate text report for a single file."""
        report = []
        report.append("=" * 70)
        report.append("CODE QUALITY ANALYSIS REPORT")
        report.append("=" * 70)
        report.append(f"File: {analysis.get('file_path', 'N/A')}")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")

        report.append("-" * 70)
        report.append("SUMMARY")
        report.append("-" * 70)
        report.append(f"Lines of Code: {analysis.get('lines_of_code', 0)}")
        report.append(f"Functions: {len(analysis.get('functions', []))}")
        report.append(f"Classes: {len(analysis.get('classes', []))}")
        report.append(f"Average Complexity: {analysis.get('complexity', 0):.2f}")
        report.append(f"Docstring Coverage: {analysis.get('docstring_coverage', 0):.1f}%")
        report.append(f"Quality Score: {analysis.get('code_quality_score', 0):.1f}/100")
        report.append("")

        functions = analysis.get('functions', [])
        if functions:
            report.append("-" * 70)
            report.append("FUNCTIONS")
            report.append("-" * 70)
            for func in functions:
                doc_status = "[OK]" if func.get('has_docstring') else "[MISSING]"
                report.append(f"  {func['name']} (line {func['line']})")
                report.append(f"    Complexity: {func['complexity']}, "
                            f"Parameters: {func['parameters']}, "
                            f"Docstring: {doc_status}")
            report.append("")

        classes = analysis.get('classes', [])
        if classes:
            report.append("-" * 70)
            report.append("CLASSES")
            report.append("-" * 70)
            for cls in classes:
                doc_status = "[OK]" if cls.get('has_docstring') else "[MISSING]"
                report.append(f"  {cls['name']} (line {cls['line']})")
                report.append(f"    Methods: {cls['methods']}, "
                            f"Docstring: {doc_status}")
            report.append("")

        report.append("=" * 70)

        return "\n".join(report)

    def _generate_directory_text_report(self, analysis: Dict) -> str:
        """Generate text report for a directory."""
        report = []
        report.append("=" * 70)
        report.append("CODE QUALITY ANALYSIS REPORT - DIRECTORY")
        report.append("=" * 70)
        report.append(f"Directory: {analysis.get('directory', 'N/A')}")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")

        report.append("-" * 70)
        report.append("SUMMARY")
        report.append("-" * 70)
        report.append(f"Total Files: {analysis.get('total_files', 0)}")
        report.append(f"Total Lines of Code: {analysis.get('total_lines_of_code', 0)}")
        report.append(f"Total Functions: {analysis.get('total_functions', 0)}")
        report.append(f"Total Classes: {analysis.get('total_classes', 0)}")
        report.append(f"Average Complexity: {analysis.get('average_complexity', 0):.2f}")
        report.append(f"Overall Quality Score: {analysis.get('overall_quality_score', 0):.1f}/100")
        report.append("")

        files = analysis.get('files', [])
        if files:
            report.append("-" * 70)
            report.append("FILE DETAILS")
            report.append("-" * 70)
            for file_analysis in files[:10]:  # Limit to first 10 files
                report.append(f"  {file_analysis.get('file_path', 'N/A')}")
                report.append(f"    LOC: {file_analysis.get('lines_of_code', 0)}, "
                            f"Score: {file_analysis.get('code_quality_score', 0):.1f}/100")
            if len(files) > 10:
                report.append(f"  ... and {len(files) - 10} more files")
            report.append("")

        report.append("=" * 70)

        return "\n".join(report)

