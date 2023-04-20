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
