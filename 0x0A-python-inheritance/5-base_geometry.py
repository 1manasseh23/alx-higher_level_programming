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
"""


class Rectangle(BaseGeometry):
    """
    This is a function that initializes the correspornding
    attribute of the rectangle object
    Args:
        width
        height
    """
    def __init__(self, width, height):
        self.width = width
        self.height = heigh
