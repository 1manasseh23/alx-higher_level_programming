#!/usr/bin/python3
"""
This Write a class Square that defines a
square by: (based on 1-square.py)
"""


class Square:
    """
    This class square
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
    This is class property
    Attribute:
        value
    """
    @property
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an inger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
