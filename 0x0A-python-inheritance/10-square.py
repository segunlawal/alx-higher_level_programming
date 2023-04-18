#!/usr/bin/python3
"""Contains the BaseGeometry class and Rectangle subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square representation"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"area of the square"""
        return self.__size ** 2
