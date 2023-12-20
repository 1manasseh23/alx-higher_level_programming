#!/usr/bin/python3
"""
This Write a class Square that defines
a square by: (based on 4-square.py)
"""


class Square:
    """
    Instantiation with optional
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
    property setter to set it
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
    """
    Public instance method that prints in stdout
    the square with the character #
    Attribute:
        __size
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
