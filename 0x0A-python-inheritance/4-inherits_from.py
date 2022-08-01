#!/usr/bin/python3
"""Defines a subclass-checking function.
"""


def inherits_from(obj, a_class):
    """function: inherits_from.
    Args:
        obj: an object to check.
        a_class: a subclass.
    Returns:
        bool
    """
    if obj.__a_class__ == True:
        return True
    return False
