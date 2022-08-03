#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """append a string to to the end of a UTF8 text file.
    Args:
        filename (string): name of a file.
        text (string): a string to append to the file.
    Returns:
        number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
