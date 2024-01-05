#!/usr/bin/python3
"""
Rectangle that defines a rectangle by
based on 7-rectangle.py
"""


class Rectangle:
    """
    Instantiation with optional width, height, and Rectangle
    Attribute:
        width
        height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    """
    property to retrieve
    Attribute:
        self.__width
    """
    @property
    def width(self):
        return self.__width
    """
    property setter to set
    Attribute:
        value
        integer
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("widtg must be an integer")
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
    Public instance method that returns the rectangle perimeter
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
        return "\n".join([str(self.print_symbol) * self.width] * self.height)
    """
    repr() should return a string representation of the rectangle to
    be able to recreate a new instance by using eval
    Attribute:
        width
        height
    """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
    """
    Print the message Bye rectangle... when an instance
    of Rectangle is deleted
    Attribute:
        None
    """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    """
    Static method that returns the biggest rectangle based on the area
    Attribute:
        rect_1
        rect_2
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
