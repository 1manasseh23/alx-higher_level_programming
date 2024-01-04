#!/usr/bin/python3
"""
Rectangle that defines a rectangle
"""


class Rectangle:
    """
    An instantiation with optional width and height
        Attribut:
            width
            height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """
    property to retrieve it
    Attribute:
        self.__height
    """
    @property
    def height(self):
        return self.__height
    """
    property setter to set it
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
            self.___height = value
    """
    property to retrieve it
        Attribute:
            self.width
    """
    @property
    def width(self):
        return self.__width
    """
    property setter to set it
    Attribute:
        value
        intenger
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("wtdth must be an integer")
        elif value < 0:
            raise ValueError("width must be >= o")
        else:
            self.__width = value
