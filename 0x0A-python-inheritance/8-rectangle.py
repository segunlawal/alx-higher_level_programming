#!/usr/bin/python3
"""contains the BaseGeometry class and Rectangle subclass"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle"""
    def __init__(self, width, height):
        """rectangle instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
