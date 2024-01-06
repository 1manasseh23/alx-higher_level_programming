#!/usr/bin/python3
"""
Rectangle that defines a rectangle by
based on 2-rectangle.py
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
    property to retrieve
    Attribute:
        self.__width
    """
    @property
    def width(self):
        return self.__width
    """
    Setter to sedth.setter
    Attribute:
        value
        integer
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    """
    property to retrieve
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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    """
    Public instance method that returns the rectangle area
    Attribute:
        width
        height
    """
    def area(self):
        return self.width * self.height
    """
    Public instance method that returns the rectangle perimete
    Attribute:
        width
        height
    """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    """
    print and str should print the rectangle with the character #
    Attribute:
        width
        height
    """
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)
