#!/usr/bin/python3
"""
Modulen 10-square.py
Defines a Square class that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle

"""
Square that inherits from Rectangle 9-rectangle.py
Attribute:
    Rectangle
"""


class Square(Rectangle):
    """
    Instantiation with size
    Attribute:
        size
    """
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

    """
    Return the string representation of the Square instance
    """
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    """
    Computes the area of the Square instance
    """
    def area(self):
        return self.__size ** 2

    """
    Validates the value of Square attribute
    Attribute
        name
        value
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} mustbe > 0".format(name))
