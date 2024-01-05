#!/usr/bin/python3
"""
This is a function that prevents the user from dynamically
creating new instance attributes
Attribute:
    first_name
"""


class LockedClass:
    __slots__ = ['first_name']
