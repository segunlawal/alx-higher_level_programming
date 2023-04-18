#!/usr/bin/python3
"""contains inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    Args:
        obj: object
        a_class: class
    Return:
        True or False
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
