#!/usr/bin/python3
"""
This is a function that returns the list of available
attributes and methods of an object
Attribute:
    obj
"""


def lookup(obj):
    return [attr for attr in dir(obj)]
