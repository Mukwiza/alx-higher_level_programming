#!/usr/bin/python3
"""Defines a file-writing function using a json representation."""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file.
    Args:
        my_obj: object.
        filename: name of the file.
    Returns:
        None.
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
