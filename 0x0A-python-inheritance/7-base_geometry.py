#!/usr/bin/python3
"""Contains BaseGeometry class"""


class BaseGeometry:
    """class with public instance method"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value
        Args:
            name: string
            value: value
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        
