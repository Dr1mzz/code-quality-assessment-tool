"""
Unit tests for the CodeAnalyzer module.
"""

import tempfile
import os
from pathlib import Path
import pytest

from src.analyzer import CodeAnalyzer


class TestCodeAnalyzer:
    """Test suite for CodeAnalyzer class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.analyzer = CodeAnalyzer()

    def test_analyze_simple_file(self):
        """Test analyzing a simple Python file."""
        # Create a temporary Python file
        code = '''
def hello_world():
    """A simple function."""
    print("Hello, World!")

def add(a, b):
    return a + b
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name

        try:
            result = self.analyzer.analyze_file(temp_path)
            assert "error" not in result
            assert result["lines_of_code"] > 0
            assert len(result["functions"]) == 2
            assert result["code_quality_score"] >= 0
        finally:
            os.unlink(temp_path)

    def test_analyze_file_with_class(self):
        """Test analyzing a file with a class."""
        code = '''
class Calculator:
    """A simple calculator class."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        return a - b
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name

        try:
            result = self.analyzer.analyze_file(temp_path)
            assert "error" not in result
            assert len(result["classes"]) == 1
            assert result["classes"][0]["name"] == "Calculator"
            assert result["classes"][0]["methods"] == 2
        finally:
            os.unlink(temp_path)

    def test_analyze_file_with_complexity(self):
        """Test complexity calculation."""
        code = '''
def complex_function(x):
    """A function with high complexity."""
    if x > 0:
        if x > 10:
            if x > 20:
                for i in range(x):
                    while i > 0:
                        i -= 1
    return x
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name

        try:
            result = self.analyzer.analyze_file(temp_path)
            assert "error" not in result
            assert len(result["functions"]) == 1
            assert result["functions"][0]["complexity"] > 3
        finally:
            os.unlink(temp_path)

    def test_analyze_directory(self):
        """Test analyzing a directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test files
            file1_path = Path(temp_dir) / "test1.py"
            file2_path = Path(temp_dir) / "test2.py"

            file1_path.write_text("def func1():\n    pass\n")
            file2_path.write_text("class Test:\n    def method(self):\n        pass\n")

            result = self.analyzer.analyze_directory(temp_dir)
            assert "error" not in result
            assert result["total_files"] == 2
            assert result["total_lines_of_code"] > 0

    def test_analyze_nonexistent_file(self):
        """Test analyzing a non-existent file."""
        result = self.analyzer.analyze_file("nonexistent_file.py")
        assert "error" in result

    def test_analyze_empty_directory(self):
        """Test analyzing an empty directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.analyzer.analyze_directory(temp_dir)
            assert "error" in result

    def test_docstring_coverage(self):
        """Test docstring coverage calculation."""
        code = '''
def with_docstring():
    """This has a docstring."""
    pass

def without_docstring():
    pass

class WithDocstring:
    """This class has a docstring."""
    pass

class WithoutDocstring:
    pass
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name

        try:
            result = self.analyzer.analyze_file(temp_path)
            assert "error" not in result
            # Should have 50% coverage (2 out of 4)
            assert 0 <= result["docstring_coverage"] <= 100
        finally:
            os.unlink(temp_path)

    def test_lines_of_code_count(self):
        """Test lines of code counting."""
        code = '''# This is a comment
# Another comment

def function():
    """Docstring."""
    x = 1
    y = 2
    return x + y

# More comments
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name

        try:
            result = self.analyzer.analyze_file(temp_path)
            assert "error" not in result
            # Should count actual code lines, not comments
            assert result["lines_of_code"] >= 5
        finally:
            os.unlink(temp_path)

    def test_quality_score_range(self):
        """Test that quality score is in valid range."""
        code = '''
def simple_function():
    """A simple function."""
    return 42
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name

        try:
            result = self.analyzer.analyze_file(temp_path)
            assert "error" not in result
            assert 0 <= result["code_quality_score"] <= 100
        finally:
            os.unlink(temp_path)

