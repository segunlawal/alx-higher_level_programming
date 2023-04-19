#!/usr/bin/python3
"""Contains append_write function"""


def append_write(filename="", text=""):
    """appends string to a text file
    Args:
        filename: name of file
        text: string
        Returns:
            number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
