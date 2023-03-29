#!/usr/bin/python3
""""This module defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """Initialization method
        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Get area of the square
        Returns:
            current square area
        """
        return (self.__size**2)
