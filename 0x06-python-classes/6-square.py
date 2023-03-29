#!/usr/bin/python3
""""This module defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization method
        Args:
            size: size of the square
            position: position of square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return (self.__position)

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

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Get area of the square
        Returns:
            current square area
        """
        return (self.__size**2)

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for i in range(self.size):
                for _ in range(self.position[0]):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print()
