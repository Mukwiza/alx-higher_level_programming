#!/usr/bin/python3
"""Defines a class-checking function.
"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an intance of, or if the object is an instance of a class that inherited from, the specified class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to check if it match with given type of object.
    Returns:
        If the object is an instance of, or if the object is an instance of a class that inherited from, the specified class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
