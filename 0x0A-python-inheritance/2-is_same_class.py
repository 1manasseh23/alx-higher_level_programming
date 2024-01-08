#!/usr/bin/python3
"""
Thi is a function that return True if the object is
exactly an instance of the specified class
Attribute:
    obj
    a_class
"""


def is_same_class(obj, a_class):
    return type(obj) == a_class
