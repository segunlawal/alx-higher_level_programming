#!/usr/bin/python3
"""Contains to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation
    of an object
    Args:
        my_obj: object or string
    """
    return (json.dumps(my_obj))
