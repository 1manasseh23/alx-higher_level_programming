#!/usr/bin/python3
"""
This is used to generate a unique identifier for instances
This is to import our base.py module from models directory
"""
import uuid
from models.base import Base
"""
Class Rectangle inherits from Base
"""


class Rectangle(Base):
    """
    Class constructor Private instance attributes,
    each with its own public getter and setter
    Attribute:
        width
        height
        x
        y
        id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id

    """
    Update the class Rectangle by adding validation of all
    setter methods and instantiation 'id excluded'
    Arguments:
        args
        kwargs
    """
    def update(self, *args, **kwargs):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)

    """
    This is a method to get the attribute width
    Return:
        __width
    """
    @property
    def width(self):
        return self.__width

    """
    This is a method to set value to attribute width
    Atrribute:
        value
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    """
    This is a method to get the attribute height
    Return:
        __height
    """
    @property
    def height(self):
        return self.__height

    """
    This is a method to set value to attribute height
    Atrribute:
        value
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    """
    This is a method to get the attribute x
    Return:
        __x
    """
    @property
    def x(self):
        return self.__x

    """
    This is a method to set value to attribute x
    Atrribute:
        value
    """
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            ValueError("x must be >= 0")
        else:
            self.__x = value

    """
    This is a method to get the attribute y
    Return:
        __y
    """
    @property
    def y(self):
        return self.__y

    """
    This is a method to set value to attribute y
    Atrribute:
        value
    """
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    """
    Thi si a function that returns the area value of
    the Rectangle instance
    Return:
        width * height
    """
    def area(self):
        return self.width * self.height

    """
    Display is a that prints in stdout the Rectangle instance with the
    character # - you don’t need to handle x and y here
    """
    def display(self):
        for i in range(self.height):
            print("#" * self.width)
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    """
    This functio is a class Rectangle by overriding the __str__ method
    Return:
        f'Rectangle id {x}/{y} - {width}/{height}'
    """
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
           f"{self.width}/{self.height}"


"""
    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width )
"""
