#!/usr/bin/python3
"""Defines a MyList class"""


class MyList:
    """This class inherits from list"""
    def __init__(self):
        """Initialize object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
