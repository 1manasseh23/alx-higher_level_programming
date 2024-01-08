#!/usr/bin/python3
"""
This is a function that returns the list of available
attributes and methods of an object
Attribute:
    obj
Returns: A list object
"""


def lookup(obj):
    """
    Attribute:
        obj
    Returns: A list object
    """
    return [attr for attr in dir(obj)]
