#!/usr/bin/python3
"""
Rectangle that defines a rectangle by based
on 1-rectangle.py
"""


class Rectangle:
    """
    Instantiation with optional width and height
    Attribute:
        width
        height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """
    property to retrieve it
    Attribute:
        self.__width
    """
    @property
    def width(self):
        return self.__width
    """
    property to set
    Attribute:
        value
        integer
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("with must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    """
    property to retrieve it
    Attribute:
        self.__height
    """
    @property
    def height(self):
        return self.__height
    """
    property setter to set
    Attribute:
        value
        integer
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TYpeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    """
    Public instance method that returns the rectangle area
    Attribute:
        self.width * self.height
    """
    def area(self):
        return self.width * self.height
    """
    Public instance method that returns the rectangle perimeter
    Attribute:
        width
        height
    """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
