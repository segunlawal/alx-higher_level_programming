#!/usr/bin/python3
""""This module defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """Initialization method
        Args:
            size: size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        def area(self):
            """Get area of the square
            Returns:
                current square area
            """
            return self.__size**2
