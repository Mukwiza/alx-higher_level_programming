#!/usr/bin/python3
"""Module: 4-inherits_from."""

def inherits_from(obj, a_class):
    """Class inherits from parent class.
    Args:
        obj: an object to check.
        a_class: a class.
    Returns:
        None
    """
    return type(obj) != a_class and isinstance(obj, a_class)
