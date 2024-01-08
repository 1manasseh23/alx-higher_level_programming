#!/usr/bin/python3
"""
This an empty class BaseGeometry
"""


class BaseGeometry:
    pass


"""
This Rectangle is a class that inherits from BaseGeometry
Attribute:
    baseGeometry
    width
    height
"""


class Rectangle(BaseGeometry):
    """
    This is a function that initializes the correspornding
    attribute of the rectangle object
    Attribute:
        width
        height
    """
    def __init__(self, width, height):
        self.width = width
        self.height = heigh
