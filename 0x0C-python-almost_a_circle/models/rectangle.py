#!/usr/bin/python3
"""Contains a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from
    Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.__width, self.__height))

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        if kwargs:
            keys = kwargs.keys()
            if 'id' in keys:
                self.id = kwargs['id']
            if 'width' in keys:
                self.width = kwargs['width']
            if 'height' in keys:
                self.height = kwargs['height']
            if 'x' in keys:
                self.x = kwargs['x']
            if 'y' in keys:
                self.y = kwargs['y']
