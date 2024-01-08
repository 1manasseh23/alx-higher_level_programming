#!/usr/bin/python3
"""
This is a function that returns True
Attribute:
    obj
    a_class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class ; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
