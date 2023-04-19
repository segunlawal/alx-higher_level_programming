#!/usr/bin/python3
"""Defines class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description of object"""
    return obj.__dict__
