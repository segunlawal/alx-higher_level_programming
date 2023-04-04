#!/usr/bin/python3
""""This module defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantation
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return (rectangle)
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """string representation of rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print message when an instance is deleted"""
        type(self).number_of_instances -= 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle based on the area
        Args:
            rect_1: instance of Rectangle
            rect_2: instance of Rectangle
        Returns:
            bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()

        if rect_1_area == rect_2_area:
            return rect_1
        elif rect_1_area > rect_2_area:
            return rect_1
        else:
            return rect_2
    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance
        Args:
            cls: rectangle instance name
            size: width and height of Rectangle
        Return:
            new Rectangle instance
        """
        return cls(size, size)
