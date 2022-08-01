#!/usr/bin/pyhton3
"""
function that returns true if object is class instance
"""


def is_same_class(obj, a_class):
    """
    function: is_same_class
    return True if object is instance of a class
    """
    if isinstance(obj, a_class):
        if obj.__class__ == a_class:
            return True
