#!/usr/bin/python3
"""
This Write a class Square that defines
a square by: (based on 5-square.py)
"""


class Square:
    """
    Instantiation with optional size and optional position
    Attribute:
        position: This is Private instance
        size: This is Private instance attribut
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    """
    property to retrieve it
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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """
    property to retrieve it
    Attribute:
        __size
    """
    @property
    def position(self):
        return self.__position
    """
    property setter to set it
    Attribute:
        value
    """
    @position.setter
    def position(self, value):
        if not (
                isinstance(value, tuple)
                and len(value) == 2
                and all(isinstance(val, int) and val >= 0 for val in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    """
    Public instance method that returns the current square area
    Attribute:
        __size
    """
    def area(self):
        return self.__size ** 2
    """
    Public instance method that prints in stdout the square
    with the character #
    Attribute:
        __size
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
