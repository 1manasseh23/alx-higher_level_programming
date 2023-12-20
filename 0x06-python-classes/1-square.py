#!/usr/bin/python3
"""
This Write a class Square that defines
a square by: (based on 0-square.py
"""


class Square:
    """
    This is a Square class
    Attribute:
        size
    """
    def __init__(self, size):
        self.__size = size
    """"
    This initialize the base class part
    Attribute:
        size
    """
    def get_size(self):
        return self.__size
    """"
    This to get Private instance attribute: size
    Attribute:
        size
    """
    def set_size(self, ptr_size):
        self.__size = ptr_size
    """
    This set a Private instance
    Attribute:
        size
    """
