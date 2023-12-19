#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an inger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an inger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value