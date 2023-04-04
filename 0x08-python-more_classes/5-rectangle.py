#!/usr/bin/python3
""""This module defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantation
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return (rectangle)
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """string representation of rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print message when an instance is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)
