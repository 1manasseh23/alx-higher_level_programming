#!/usr/bin/python3
"""
This provides a way to generate unique
identifiers (UUIDs) for objects
"""

import uuid

"""
Base is a perent class with a private class attribute
Attribute:
    __nb_objects
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This initialize the class Base by id
        Attribute:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
