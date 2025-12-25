"""
Main entry point for Code Quality Assessment Tool.

This script provides a command-line interface for analyzing Python code quality.
"""

import argparse
import sys
from pathlib import Path

from src.analyzer import CodeAnalyzer
from src.reporter import ReportGenerator


def main():
    """Main function to run the code quality analyzer."""
    parser = argparse.ArgumentParser(
        description="Code Quality Assessment Tool - Analyze Python code quality"
    )
    parser.add_argument(
        "target",
        type=str,
        help="File or directory to analyze"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Output file path for report"
    )
    parser.add_argument(
        "--format",
        "-f",
        type=str,
        choices=["text", "json"],
        default="text",
        help="Output format (text or json)"
    )
    parser.add_argument(
        "--report-dir",
        type=str,
        default="reports",
        help="Directory to save reports (default: reports)"
    )

    args = parser.parse_args()

    # Check if target exists
    target_path = Path(args.target)
    if not target_path.exists():
        print(f"Error: {args.target} does not exist", file=sys.stderr)
        return 1

    # Initialize analyzer and reporter
    analyzer = CodeAnalyzer()
    reporter = ReportGenerator(output_dir=args.report_dir)

    # Analyze
    if target_path.is_file():
        if not target_path.suffix == ".py":
            print("Error: Target file must be a Python file (.py)", file=sys.stderr)
            return 1
        print(f"Analyzing file: {args.target}")
        analysis = analyzer.analyze_file(str(target_path))
    else:
        print(f"Analyzing directory: {args.target}")
        analysis = analyzer.analyze_directory(str(target_path))

    # Generate report
    if "error" in analysis:
        print(f"Error during analysis: {analysis['error']}", file=sys.stderr)
        return 1

    if args.format == "json":
        report = reporter.generate_json_report(analysis, output_file=args.output)
    else:
        report = reporter.generate_text_report(analysis, output_file=args.output)

    # Print report to stdout if no output file specified
    if args.output is None:
        print(report)

    print("\nAnalysis complete!", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

