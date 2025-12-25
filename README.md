# Code Quality Assessment Tool

[![Tests](https://github.com/Dr1mzz/code-quality-assessment-tool/actions/workflows/tests.yml/badge.svg)](https://github.com/Dr1mzz/code-quality-assessment-tool/actions/workflows/tests.yml)
[![Scheduled Analysis](https://github.com/Dr1mzz/code-quality-assessment-tool/actions/workflows/scheduled-analysis.yml/badge.svg)](https://github.com/Dr1mzz/code-quality-assessment-tool/actions/workflows/scheduled-analysis.yml)

A comprehensive Python tool for automatically assessing code quality in Python projects. This tool analyzes code metrics including PEP8 compliance, cyclomatic complexity, docstring coverage, and generates detailed reports.

## 📋 Description

The Code Quality Assessment Tool is designed to help developers, educators, and students evaluate the quality of their Python code. It provides automated analysis of various code quality metrics and generates both human-readable and machine-processable reports.

### Key Features

- **Cyclomatic Complexity Analysis**: Calculates complexity metrics for functions and methods
- **Docstring Coverage**: Measures the percentage of functions and classes with documentation
- **Code Metrics**: Provides statistics on lines of code, functions, classes, and more
- **Quality Scoring**: Generates an overall quality score (0-100) based on multiple factors
- **Multiple Report Formats**: Supports both text and JSON output formats
- **Batch Processing**: Can analyze single files or entire directories
- **CI/CD Integration**: Includes GitHub Actions workflows for automated analysis

### Use Cases

- **Educational Context**: Help students understand code quality metrics and improve their coding practices
- **Code Review**: Automated preliminary code quality assessment before manual review
- **Continuous Improvement**: Track code quality trends over time through scheduled analysis
- **Project Health Monitoring**: Regular analysis of codebase quality in development teams

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**:
```bash
git clone <repo-url>
cd code-quality-assessment-tool
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

Analyze a single Python file:
```bash
python -m src.main path/to/file.py
```

Analyze an entire directory:
```bash
python -m src.main path/to/directory/
```

### Command-Line Options

```
usage: main.py [-h] [--output OUTPUT] [--format {text,json}] [--report-dir REPORT_DIR] target

positional arguments:
  target                File or directory to analyze

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file path for report
  --format {text,json}, -f {text,json}
                        Output format (text or json). Default: text
  --report-dir REPORT_DIR
                        Directory to save reports (default: reports)
```

### Examples

#### Example 1: Analyze a single file with text output

```bash
python -m src.main src/analyzer.py
```

**Output:**
```
======================================================================
CODE QUALITY ANALYSIS REPORT
======================================================================
File: src/analyzer.py
Generated: 2025-12-25 17:00:00

----------------------------------------------------------------------
SUMMARY
----------------------------------------------------------------------
Lines of Code: 245
Functions: 8
Classes: 1
Average Complexity: 3.2
Docstring Coverage: 87.5%
Quality Score: 82.3/100

----------------------------------------------------------------------
FUNCTIONS
----------------------------------------------------------------------
  analyze_file (line 25)
    Complexity: 2, Parameters: 1, Docstring: ✓
  analyze_directory (line 58)
    Complexity: 4, Parameters: 1, Docstring: ✓
  ...

======================================================================
```

#### Example 2: Analyze a directory and save JSON report

```bash
python -m src.main src/ --format json --output analysis_report.json
```

**Output** (excerpt from JSON):
```json
{
  "timestamp": "2025-12-25T17:00:00",
  "analysis": {
    "directory": "src/",
    "total_files": 3,
    "total_lines_of_code": 580,
    "total_functions": 15,
    "total_classes": 2,
    "average_complexity": 2.8,
    "overall_quality_score": 85.2,
    "files": [...]
  }
}
```

#### Example 3: Analyze sample code

```bash
python -m src.main data/sample.py --format text
```

This will analyze the sample Python file included in the repository and display the results.

### Programmatic Usage

You can also use the tool programmatically in your Python code:

```python
from src.analyzer import CodeAnalyzer
from src.reporter import ReportGenerator

# Initialize analyzer
analyzer = CodeAnalyzer()

# Analyze a file
results = analyzer.analyze_file("path/to/file.py")

# Generate report
reporter = ReportGenerator()
text_report = reporter.generate_text_report(results)
print(text_report)

# Or generate JSON
json_report = reporter.generate_json_report(results, output_file="report.json")
```

## 📁 Project Structure

```
.
├── src/                    # Source code
│   ├── __init__.py
│   ├── analyzer.py         # Main analysis logic
│   ├── reporter.py         # Report generation
│   └── main.py             # CLI entry point
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_analyzer.py    # Tests for analyzer
│   ├── test_reporter.py    # Tests for reporter
│   └── test_main.py        # Integration tests
├── data/                   # Sample data files
│   └── sample.py           # Sample Python file for testing
├── docs/                   # Documentation
├── reports/                # Generated reports (gitignored)
├── .github/
│   └── workflows/          # GitHub Actions workflows
│       ├── tests.yml       # Standard CI/CD workflow
│       └── scheduled-analysis.yml  # Scheduled analysis workflow
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔧 Requirements

### Python Version
- Python 3.8 or higher

### Dependencies

Core dependencies are listed in `requirements.txt`:

- **numpy** >= 1.20.0 - Numerical computing
- **pandas** >= 1.3.0 - Data manipulation
- **flake8** >= 4.0.0 - Code linting
- **black** >= 22.0.0 - Code formatting
- **pytest** >= 7.0.0 - Testing framework
- **pytest-cov** >= 3.0.0 - Test coverage

For the complete list, see `requirements.txt`.

## 🧪 Testing

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=src --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_analyzer.py -v
```

Run tests with verbose output:
```bash
pytest -v
```

## 🔄 CI/CD Workflows

This project includes two GitHub Actions workflows:

### 1. Tests and Code Quality (`tests.yml`)

This workflow runs on every push and pull request:

- Runs tests on Python 3.8, 3.9, 3.10, and 3.11
- Performs code linting with flake8
- Checks code formatting with black
- Generates test coverage reports
- Uploads coverage to Codecov

**Status Badge:** 
```
![Tests](https://github.com/Dr1mzz/code-quality-assessment-tool/actions/workflows/tests.yml/badge.svg)
```

### 2. Scheduled Code Analysis (`scheduled-analysis.yml`)

This creative workflow demonstrates advanced CI/CD usage:

**Features:**
- **Scheduled execution**: Runs daily at 2 AM UTC
- **Manual trigger**: Can be triggered manually via `workflow_dispatch` with custom parameters
- **Artifact upload**: Uploads analysis reports as downloadable artifacts
- **Auto-commit**: Automatically commits reports to a `reports` branch on scheduled runs
- **Summary generation**: Creates GitHub Actions summary with report preview

**Manual Trigger:**
1. Go to Actions → Scheduled Code Analysis
2. Click "Run workflow"
3. Optionally specify:
   - Target directory (default: `src`)
   - Report format (text or json)

**Use Case:** This workflow automatically monitors code quality over time, making it easy to track improvements or regressions in code quality metrics.

## 📊 Code Quality Metrics Explained

### Cyclomatic Complexity

Measures the complexity of functions by counting decision points (if, while, for, etc.). Lower values indicate simpler, more maintainable code.

- **1-5**: Simple
- **6-10**: Moderate
- **11-20**: Complex
- **21+**: Very complex

### Docstring Coverage

Percentage of functions and classes that have docstrings. Higher coverage indicates better documentation.

### Quality Score

An overall score (0-100) calculated from:
- Complexity (lower is better)
- Docstring coverage (higher is better)
- Function parameter count (fewer is better)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Ensure code follows style guidelines (`flake8`, `black`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## 📝 License

This project is created as an educational assignment. Feel free to use and modify as needed.

## 👤 Author

Student Project - Code Quality Assessment Tool

## 🙏 Acknowledgments

- Built as part of a programming assignment focusing on code quality, CI/CD, and best practices
- Inspired by tools like pylint, flake8, and radon
- Uses Python's AST module for code analysis

## 📚 Additional Resources

- [Python AST Documentation](https://docs.python.org/3/library/ast.html)
- [PEP 8 Style Guide](https://pep8.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Pytest Documentation](https://docs.pytest.org/)

---

**Note:** Badge URLs уже настроены для репозитория `code-quality-assessment-tool`. Если вы используете другое название, обновите URLs в строках 3-4.

