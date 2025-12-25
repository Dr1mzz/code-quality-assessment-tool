"""
Integration tests for the main module.
"""

import tempfile
import sys
from pathlib import Path
import subprocess

import pytest


class TestMainModule:
    """Test suite for main module integration."""

    def test_main_with_file(self):
        """Test main function with a file argument."""
        code = '''
def test_function():
    """Test function."""
    return 42
'''
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_path = f.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "src.main", temp_path],
                capture_output=True,
                text=True
            )
            # Should complete without error
            assert result.returncode == 0 or result.returncode is None
        finally:
            Path(temp_path).unlink()

    def test_main_with_directory(self):
        """Test main function with a directory argument."""
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "test.py"
            test_file.write_text("def func(): pass\n")

            result = subprocess.run(
                [sys.executable, "-m", "src.main", temp_dir],
                capture_output=True,
                text=True
            )
            # Should complete without error
            assert result.returncode == 0 or result.returncode is None

