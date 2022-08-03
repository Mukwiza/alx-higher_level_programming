#!/usr/bin/python3
"""Defines function that creates an object form a json file."""
import json


def load_from_json_file(filename):
    """creates an object.
    Args:
        filename: name of a json file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
       return json.load(f)
