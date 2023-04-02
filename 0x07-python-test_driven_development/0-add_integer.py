#!/usr/bin/python3
"""Addition of two integers"""


def add_integer(a, b=98):
    """Add two integers
    Args:
        a: first number
        b: second number
    Returns:
        sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
