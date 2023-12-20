#!/usr/bin/python3
"""
This Write a class Square that defines
a square by: (based on 4-square.py)
"""


class Square:
    """
    Instantiation with size
    Attribute:
        size
    """
    def __init__(self, size=0):
        self.size = size
    """
    property to retrieve
    Attribute:
        __size
    """
    @property
    def size(self):
        return self.__size
    """
    property setter to set
    Attribute:
        value
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    Public instance method that returns the current square area
    Attribute:
        __size
    """
    def area(self):
        return self.__size ** 2
    """
    This method compares if the area of the current square,
    is equal to the area of another square
    It returns True if they are equal, False otherwise.
    Attribute:
        other
    """
    def __eq__(self, other):
        return self.area() == other.area()
    """
    This method checks if the area of the current square,
    is not equal to the area of another square
    It returns True if they are not equal, False otherwise.
    Attribute:
        other
    """
    def __ne__(self, other):
        return self.area() != other.area()
    """
    This method verifies if the area of the current square,
    is less than the area of another square
    It returns True if the current square's area is smaller,
    False otherwise
    Attribute:
        other
    """
    def __lt__(self, other):
        return self.area() < other.area()
    """
    This method checks if the area of the current square,
    is less than or equal to the area of another square
    It returns True if the current square's area is smaller
    or equal, False otherwise.
    Attribute:
        other
    """
    def __le__(self, other):
        return self.area() <= other.area()
    """
    This method confirms if the area of the current square,
    is greater than the area of another square
    It returns True if the current square's area is larger,
    False otherwise
    Attribute:
        other
    """
    def __gt__(self, other):
        return self.area() > other.area()
    """
    This method checks if the area of the current square,
    is greater than or equal to the area of another square
    It returns True if the current square's area is larger or equal,
    False otherwise.
    Attribute:
        other
    """
    def __ge__(self, other):
        return self.area() >= other.area()
