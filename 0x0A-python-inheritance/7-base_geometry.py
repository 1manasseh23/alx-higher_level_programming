#!/usr/bin/python3
"""
class BaseGeometry based on 6-base_geometry.py
"""


class BaseGeometry:
    """
    Public instance method that raises an Exception with
    the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implement")

    """
    Public instance method that validates value
    Attribute:
        name
        vlue
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
Rectangle is a class that inherits from BaseGeometry
Attribute:
    BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    This is a class that initializes the attribute of Rectangle
    Attribute:
        width
        height
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    """
    This function calculates the area of rectangle base on
    its width and height
    """
    def area(self):
        return self.width * self.height
