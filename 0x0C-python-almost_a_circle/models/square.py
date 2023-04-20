#!/usr/bin/python3
"""Contains a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from
    Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method
        Args:
            x: x position
            y: y position
            size: width and height of square
        """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return (self.__width)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
