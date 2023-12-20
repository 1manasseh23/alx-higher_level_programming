#!/usr/bin/python3
"""
This Write a class Square that defines
a square by: (based on 6-square.py)
"""


class Square:
    """
    Instantiation with optional size and optional position
    Attribute:
        size: Private instance attribute
        position: Private instance attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    """
    property def size to retrieve
    Attribute:
        __size
    """
    @property
    def size(self):
        return self.__size
    """
    property setter  to set
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
    property to retrieve
    Attribute:
        __position
    """
    @property
    def position(self):
        return self.__position
    """
    property setter to set
    Attribute:
        value
    """
    @position.setter
    def position(self, value):
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(j, int) for j in value)
                or not all(j >= 0 for j in value)
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
    Public instance method that prints
    in stdout the square with the character #
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
    """
    This is a special method it's called on an instance of a class
    Attribute:
        __size
    """
    def __str__(self):
        square_representation = ""
        if self.__size == 0:
            square_representation += "\n"
        else:
            for _ in range(self.__position[1]):
                square_representation += "\n"
            square_representation = ""
            for _ in range(self.__size):
                line = " " * self.__position[0] + "#" * self.__size + "\n"
                square_representation += line
            return square_representation.rstrip()
