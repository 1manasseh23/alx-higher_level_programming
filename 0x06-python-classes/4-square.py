#!/usr/bin/python3
"""
This Write a class Square that defines
a square by: (based on 3-square.py)
"""


class Square:
    """
    Instantiation with optional size 
    Attribute:
        size
    """
    def __init__(self, size=0):
        self.size = size
    """
    This is a class property
    Attribute:
        size
    """
    @property
    def size(self):
        return self.__size
    """
    This is a property to retrieve it
    Attribute:
        value
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an inger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """
    Public instance method that returns the current square area
    Attribute:
        __size
    """
    def area(self):
        return self.__size ** 2
