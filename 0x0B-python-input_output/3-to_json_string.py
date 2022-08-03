#!/usr/bin/python3
"""Defines function that returns the JSON representation of an object."""


def to_json_string(my_obj):
    """json representation.
    Args:
        my_obj (string): object.
    Returns:
        JSON representation o an object.
    """
    import json
    return json.dumps(my_obj)

