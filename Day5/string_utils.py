"""
string_utils.py
---------------
This module provides utility functions for string processing.
Useful in text preprocessing and NLP tasks.
"""

def to_upper(text):
    """Converts a string to uppercase."""
    return text.upper()

def to_lower(text):
    """Converts a string to lowercase."""
    return text.lower()

def count_words(text):
    """Returns the number of words in the text."""
    return len(text.split())

def reverse_string(text):
    """Returns the reversed string."""
    return text[::-1]
