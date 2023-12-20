#!/usr/bin/python3
"""This Write a class Square that defines
a square by: (based on 0-square.py
"""
class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, ptr_size):
        self.__size = ptr_size
