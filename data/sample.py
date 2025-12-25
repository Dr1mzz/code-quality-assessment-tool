"""
Sample Python file for testing and demonstration purposes.
"""


class SampleClass:
    """A sample class for demonstration."""

    def __init__(self, value: int):
        """
        Initialize the sample class.

        Args:
            value: Initial value
        """
        self.value = value

    def add(self, other: int) -> int:
        """
        Add a value to the current value.

        Args:
            other: Value to add

        Returns:
            Sum of current value and other
        """
        return self.value + other

    def multiply(self, factor: int) -> int:
        """Multiply the current value by a factor."""
        return self.value * factor


def calculate_sum(numbers: list) -> int:
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers: List of numbers to sum

    Returns:
        Sum of all numbers
    """
    total = 0
    for num in numbers:
        total += num
    return total


def simple_function():
    """A simple function without parameters."""
    return 42

