"""
Code Quality Analyzer Module

This module provides functionality to analyze Python code quality
using various metrics including PEP8 compliance, cyclomatic complexity,
docstring coverage, and code duplication.
"""

import ast
import os
import re
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class CodeAnalyzer:
    """Main class for analyzing Python code quality."""

    def __init__(self):
        """Initialize the CodeAnalyzer."""
        self.results = {}

    def analyze_file(self, file_path: str) -> Dict:
        """
        Analyze a single Python file.

        Args:
            file_path: Path to the Python file to analyze

        Returns:
            Dictionary containing analysis results
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
        except Exception as e:
            return {"error": str(e)}

        tree = self._parse_code(code)
        if tree is None:
            return {"error": "Failed to parse code"}

        analysis = {
            "file_path": file_path,
            "lines_of_code": self._count_lines_of_code(code),
            "functions": self._analyze_functions(tree, code),
            "classes": self._analyze_classes(tree, code),
            "complexity": self._calculate_average_complexity(tree),
            "docstring_coverage": self._check_docstring_coverage(tree, code),
            "code_quality_score": 0.0
        }

        # Calculate overall quality score
        analysis["code_quality_score"] = self._calculate_quality_score(analysis)

        return analysis

    def analyze_directory(self, directory: str) -> Dict:
        """
        Analyze all Python files in a directory.

        Args:
            directory: Path to directory to analyze

        Returns:
            Dictionary containing aggregated analysis results
        """
        python_files = list(Path(directory).rglob("*.py"))
        python_files = [f for f in python_files if "__pycache__" not in str(f)]

        if not python_files:
            return {"error": "No Python files found"}

        file_analyses = []
        total_loc = 0
        total_functions = 0
        total_classes = 0
        total_complexity = 0.0

        for file_path in python_files:
            analysis = self.analyze_file(str(file_path))
            if "error" not in analysis:
                file_analyses.append(analysis)
                total_loc += analysis["lines_of_code"]
                total_functions += len(analysis["functions"])
                total_classes += len(analysis["classes"])
                total_complexity += analysis["complexity"]

        avg_complexity = total_complexity / len(file_analyses) if file_analyses else 0.0

        return {
            "directory": directory,
            "total_files": len(file_analyses),
            "total_lines_of_code": total_loc,
            "total_functions": total_functions,
            "total_classes": total_classes,
            "average_complexity": avg_complexity,
            "files": file_analyses,
            "overall_quality_score": sum(a["code_quality_score"] for a in file_analyses) / len(file_analyses) if file_analyses else 0.0
        }

    def _parse_code(self, code: str) -> Optional[ast.AST]:
        """Parse Python code into AST."""
        try:
            return ast.parse(code)
        except SyntaxError:
            return None

    def _count_lines_of_code(self, code: str) -> int:
        """Count lines of code (excluding comments and blank lines)."""
        lines = code.split('\n')
        loc = 0
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                loc += 1
        return loc

    def _analyze_functions(self, tree: ast.AST, code: str) -> List[Dict]:
        """Analyze all functions in the code."""
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_info = {
                    "name": node.name,
                    "line": node.lineno,
                    "complexity": self._calculate_complexity(node),
                    "has_docstring": ast.get_docstring(node) is not None,
                    "parameters": len(node.args.args)
                }
                functions.append(func_info)
        return functions

    def _analyze_classes(self, tree: ast.AST, code: str) -> List[Dict]:
        """Analyze all classes in the code."""
        classes = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]
                class_info = {
                    "name": node.name,
                    "line": node.lineno,
                    "methods": len(methods),
                    "has_docstring": ast.get_docstring(node) is not None
                }
                classes.append(class_info)
        return classes

    def _calculate_complexity(self, node: ast.AST) -> int:
        """Calculate cyclomatic complexity of a function."""
        complexity = 1  # Base complexity
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler,
                                ast.And, ast.Or)):
                complexity += 1
        return complexity

    def _calculate_average_complexity(self, tree: ast.AST) -> float:
        """Calculate average cyclomatic complexity of all functions."""
        complexities = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                complexities.append(self._calculate_complexity(node))
        return sum(complexities) / len(complexities) if complexities else 0.0

    def _check_docstring_coverage(self, tree: ast.AST, code: str) -> float:
        """
        Check docstring coverage for classes and functions.

        Returns:
            Percentage of functions/classes with docstrings
        """
        total = 0
        with_docstrings = 0

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                total += 1
                if ast.get_docstring(node) is not None:
                    with_docstrings += 1

        return (with_docstrings / total * 100) if total > 0 else 0.0

    def _calculate_quality_score(self, analysis: Dict) -> float:
        """
        Calculate overall code quality score (0-100).

        Factors:
        - Complexity (lower is better)
        - Docstring coverage (higher is better)
        - Function size (smaller functions are better)
        """
        score = 100.0

        # Penalize high complexity
        avg_complexity = analysis.get("complexity", 0)
        if avg_complexity > 10:
            score -= 30
        elif avg_complexity > 5:
            score -= 15
        elif avg_complexity > 3:
            score -= 5

        # Reward docstring coverage
        doc_coverage = analysis.get("docstring_coverage", 0)
        score += (doc_coverage - 50) * 0.3  # Adjust based on coverage

        # Penalize too many parameters
        for func in analysis.get("functions", []):
            if func["parameters"] > 5:
                score -= 2

        return max(0.0, min(100.0, score))

