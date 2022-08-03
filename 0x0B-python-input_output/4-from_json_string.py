#!/usr/bin/python3
"""Defines function that returns an object represented by a json string."""


def from_json_string(my_str):
    """json representation.
    Args:
        my_str : object.
    Returns:
        an object represented by a json string.
    """
    import json
    return json.loads(my_str)
