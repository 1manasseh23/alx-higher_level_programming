#!/usr/bin/python3
"""
class BaseGeometry based on 5-base_geometry.py
"""


class BaseGeometry:
    """
    Public instance method that raises an Exception
    with the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")


"""
Rectangle class is inheritance from BaseGeometry
Attribute:
    BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    This function calculates the area of a rectangle
    base on width and height
    Attribute:
        width
        height
    """
    def __init_(self, width, height):
        self.width = width
        self.height = height

    """
    calculates the area of a rectangle
    base on width and height
    """
    def area(self):
        return self.width * self.height
