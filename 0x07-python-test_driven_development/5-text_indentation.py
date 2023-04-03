#!/usr/bin/python3
"""This module indents a text"""


def text_indentation(text):
    """Indents a text
    Args:
        text: string to be indentend
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    check = 0
    for char in text:
        if check == 0:
            if char == ' ':
                continue
            else:
                check = 1
        if check == 1:
            if char == '?' or char == '.' or char == ':':
                print("{}".format(char))
                print()
                check = 0
            else:
                print(char, end="")
