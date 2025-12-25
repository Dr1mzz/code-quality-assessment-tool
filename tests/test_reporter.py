"""
Unit tests for the ReportGenerator module.
"""

import tempfile
from pathlib import Path
import json
import pytest

from src.reporter import ReportGenerator


class TestReportGenerator:
    """Test suite for ReportGenerator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.reporter = ReportGenerator(output_dir=self.temp_dir)

    def test_generate_text_report_for_file(self):
        """Test generating text report for a file analysis."""
        analysis = {
            "file_path": "test.py",
            "lines_of_code": 50,
            "functions": [
                {
                    "name": "test_func",
                    "line": 10,
                    "complexity": 2,
                    "has_docstring": True,
                    "parameters": 2
                }
            ],
            "classes": [
                {
                    "name": "TestClass",
                    "line": 5,
                    "methods": 3,
                    "has_docstring": True
                }
            ],
            "complexity": 2.5,
            "docstring_coverage": 75.0,
            "code_quality_score": 85.5
        }

        report = self.reporter.generate_text_report(analysis)
        assert isinstance(report, str)
        assert "CODE QUALITY ANALYSIS REPORT" in report
        assert "test.py" in report
        assert "50" in report
        assert "test_func" in report

    def test_generate_text_report_for_directory(self):
        """Test generating text report for a directory analysis."""
        analysis = {
            "directory": "test_dir",
            "total_files": 5,
            "total_lines_of_code": 500,
            "total_functions": 20,
            "total_classes": 5,
            "average_complexity": 3.2,
            "overall_quality_score": 78.5,
            "files": []
        }

        report = self.reporter.generate_text_report(analysis)
        assert isinstance(report, str)
        assert "DIRECTORY" in report
        assert "5" in report
        assert "500" in report

    def test_generate_text_report_save_to_file(self):
        """Test saving text report to file."""
        analysis = {
            "file_path": "test.py",
            "lines_of_code": 10,
            "functions": [],
            "classes": [],
            "complexity": 1.0,
            "docstring_coverage": 0.0,
            "code_quality_score": 50.0
        }

        output_file = "test_report.txt"
        report = self.reporter.generate_text_report(analysis, output_file=output_file)

        output_path = Path(self.temp_dir) / output_file
        assert output_path.exists()
        assert output_path.read_text() == report

    def test_generate_json_report(self):
        """Test generating JSON report."""
        analysis = {
            "file_path": "test.py",
            "lines_of_code": 10,
            "functions": [],
            "classes": [],
            "complexity": 1.0,
            "docstring_coverage": 0.0,
            "code_quality_score": 50.0
        }

        report = self.reporter.generate_json_report(analysis)
        data = json.loads(report)

        assert "timestamp" in data
        assert "analysis" in data
        assert data["analysis"]["file_path"] == "test.py"

    def test_generate_json_report_save_to_file(self):
        """Test saving JSON report to file."""
        analysis = {
            "file_path": "test.py",
            "lines_of_code": 10,
            "functions": [],
            "classes": [],
            "complexity": 1.0,
            "docstring_coverage": 0.0,
            "code_quality_score": 50.0
        }

        output_file = "test_report.json"
        report = self.reporter.generate_json_report(analysis, output_file=output_file)

        output_path = Path(self.temp_dir) / output_file
        assert output_path.exists()

        with open(output_path, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
        assert saved_data["analysis"]["file_path"] == "test.py"

    def test_error_handling_in_report(self):
        """Test handling errors in analysis results."""
        analysis = {"error": "File not found"}

        report = self.reporter.generate_text_report(analysis)
        assert "Error" in report or "error" in report.lower()

