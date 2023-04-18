#!/usr/bin/python3
"""contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an
    instance of a class that inherited from
    , the specified class
    Args:
        obj: object
        a_class: class
    Return:
        True or False
    """
    return (isinstance(obj, a_class))
