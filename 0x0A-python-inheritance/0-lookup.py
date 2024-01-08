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
    Returns  the list of available attributes and
    methods of an object
    """
    return [attr for attr in dir(obj)]
