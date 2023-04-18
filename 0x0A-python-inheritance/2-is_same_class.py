#!/usr/bin/python3
"""This module contains is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly
    an instance of the specified class
    Args:
        obj: object
        a_class: class
    """
    if(type(obj) == a_class):
        return True
    return False
