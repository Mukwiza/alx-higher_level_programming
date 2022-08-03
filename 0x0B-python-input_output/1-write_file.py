#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """ write a string to a text file.
    Args:
        filename (string): name of a text file.
        text (string): a string to write to the file.
    Returns:
        the number of characters written on the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
