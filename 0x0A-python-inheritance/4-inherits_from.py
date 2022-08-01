#!/usr/bin/python3
"""Defines a subclass-checking function.
"""


def inherits_from(obj, a_class):
    """function: inherits_from.
    Args:
        obj: an object to check.
        a_class: a class.
    Returns:
        bool
    """
    if type(obj) != a_class and isinstance(obj, a_class):
            return True
    return False
