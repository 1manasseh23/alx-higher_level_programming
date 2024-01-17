#!/usr/bin/python3
"""
This module is import from models directory used class rectangle
"""
from models.rectangle import Rectangle
"""
class Square that inherits from Rectangle
in the file models/square.py
"""


class Square(Rectangle):
    """
    Class constructor that initialize class attribute
    Attribute:
        size
        x
        y
        id
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """
    This is a method to get the attribute size
    Return:
        width
    """
    @property
    def size(self):
        return self.width

    """
    This is a method to set value to size
    Attribute:
        value
    """
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """
    This is to override the str method in the square class
    Return:
        Square "object({}) {}/{} - {}". format(id, x, y, width)
    """
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    """
    Update class Square by adding the public method that assigns attributes
    Attribute:
        args
        kwargs
    """
    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value, in kwargs.items():
                setattr(self, key, value)
