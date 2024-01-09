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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        super().__init__()

    """
    Computes the area of the rectangle
    """
    def area(self):
        return self.__width * self.__height

    """
    Return the string representation of the Square instance
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    """
    Computes the area of the Square instance
    """
    def area(self):
        return self.__size ** 2

    """
    Return the string representation of the Square instance
    """
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
