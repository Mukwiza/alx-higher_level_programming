#!/usr/bin/python3
"""Defines a class-checking function.
"""


def is_kind_of_class(obj, a_class):
    """function: is_kind_of_class
    Args:
        obj (any): The object to check.
        a_class (type): a class
    Returns:
        Bool
    """
    if isinstance(obj, a_class):
        return True
    return False
