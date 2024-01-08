#!/usr/bin/python3
"""
Module 8-rectangle.py
Defines a Rectangle class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
class Rectangle that inherits from BaseGeometry 7-base_geometry.py
Attribute:
    BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Instantiation with width and height
    Attribute:
        width
        height
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().__init__()

    """
    Return a string representation of the Rectangle instance
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    """
    Computes the area of the Rectangle instance
    """
    def area(self):
        return self.__width * self.__height

    """
    This function is amethod that validate the value of an argument
    Attribute:
        name
        value
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be  > 0".format(name))
