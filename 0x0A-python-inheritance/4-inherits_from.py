#!/usr/bin/python3
"""module: 4-inherits_from
"""

def inherits_from(obj, a_class):
    """function: inherits_from.
    Args:
        obj: an object to check.
        a_class: a class.
    Returns:
        None.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
