"""
math_utils.py
--------------
This module provides basic and advanced mathematical utility functions
commonly used in data science and machine learning.
"""

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def factorial(n):
    """Returns the factorial of n using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Returns True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
