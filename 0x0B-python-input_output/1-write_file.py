#!/usr/bin/python3
"""Contains write_file function"""


def write_file(filename="", text=""):
    """write string to a text file
    Args:
        filename: name of file
        text: string
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
