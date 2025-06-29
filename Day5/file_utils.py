"""
file_utils.py
-------------
Module for reading and writing files.
Commonly used in data loading and saving.
"""

def read_file(filepath):
    """Reads a file and returns its content as a string."""
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    """Writes content to a file."""
    with open(filepath, 'w') as f:
        f.write(content)
