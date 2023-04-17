#!/usr/bin/python3
"""Defines a MyList class"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
