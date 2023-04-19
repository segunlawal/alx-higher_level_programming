#!/usr/bin/python3
"""Contains read_file function"""


def read_file(filename=""):
    """reads a text file
    Args:
        filename: name of file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
