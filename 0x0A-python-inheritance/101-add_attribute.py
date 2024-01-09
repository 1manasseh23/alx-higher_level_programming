#!/usr/bin/python3
"""
This function adds a new attribute to an
object if it’s possible
Attribute:
    obj
    name
    value
"""


def add_attribute(obj, name, value):
    """
    Raise a TypeError exception, with the message can't
    add new attribute if the object can’t
    have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
