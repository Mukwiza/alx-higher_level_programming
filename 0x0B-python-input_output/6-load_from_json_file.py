#!/usr/bin/python3
"""Defines function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """creates an object.
    Args:
        filename: name of a JSON file.
    """
    with open(filename) as f:
       return json.load(f)
