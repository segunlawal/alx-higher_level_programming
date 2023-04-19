#!/usr/bin/python3
"""Contains from_json_string function"""
import json


def from_json_string(my_str):
    """Returns an object
    represented by a JSON string
    Args:
        my_str: string
    """
    return (json.loads(my_str))
