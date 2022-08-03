#!/usr/bin/python3
"""Function that reads file."""


def read_file(filename=""):
    """Opening and reading file.
    Args:
        filename (string): name of a file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
       print(f.read(), end='')
