def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
import math


def std(numbers):
    """Calculate population standard deviation (using N in denominator)."""
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return math.sqrt(variance)
