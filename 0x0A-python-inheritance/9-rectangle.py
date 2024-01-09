#!/usr/bin/python3
"""
Modulen 9-rectangle.py
Defines a Rectangle class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Rectangle that inherits from BaseGeometry 7-base_geometry.py
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
    Return the string representation of the Rectangle instance
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    """
    Computes the area of the Rectangle instance
    """
    def area(self):
        return self.__width * self.__height

    """
    Validates the value of Rectangle attribute
    Attribute
        name
        value
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} mustbe > 0".format(name))
