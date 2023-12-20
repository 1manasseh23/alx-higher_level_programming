#!/usr/bin/python3
"""
This Write a class Square that defines
a square by: (based on 2-square.py)
"""


class Square:
    """
    This is a class square
    Attribute:
        size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an inger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    Public instance method that returns the current square area
    Attribute:
        __size
    """
    def area(self):
        return self.__size ** 2
