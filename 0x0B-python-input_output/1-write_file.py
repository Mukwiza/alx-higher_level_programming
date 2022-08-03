#!/usr/bin/python3
"""Function that writes a string to a text file."""


def write_file(filename="", text=""):
    """write a string to text file and return number of characters.
    Args:
        filename = name of a file.
        text = a string to write in text file.
    Return:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
      return (f.write(text))
