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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        if kwargs:
            keys = kwargs.keys()
            if 'id' in keys:
                self.id = kwargs['id']
            if 'size' in keys:
                self.size = kwargs['size']
            if 'x' in keys:
                self.x = kwargs['x']
            if 'y' in keys:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
