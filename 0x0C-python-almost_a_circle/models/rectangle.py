#!/usr/bin/python3
"""
Class Rectangle inherits from Base
"""
import uuid
from models.base import Base
import csv


class Rectangle(Base):
    """
    Class constructor Private instance attributes
    each with its own public getter and setter
    Attribute:
        width
        height
        x
        y
        id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This initialize the class rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def to_dictionary(self):
        """
        This is a function that return dictionary
        Return:
            id
            width
            height
            x
            y
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
            }

        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id

    @property
    def width(self):
        """
        This is a method to get the attribute width
        Return:
            __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is a method to set value to attribute width
        Atrribute:
            value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        This is a method to get the attribute height
        Return:
            __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is a method to set value to attribute height
        Atrribute:
            value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        This is a method to get the attribute x
        Return:
            __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is a method to set value to attribute x
        Atrribute:
            value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        This is a method to get the attribute y
        Return:
            __y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is a method to set value to attribute y
        Atrribute:
            value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding validation of all
        setter methods and instantiation 'id excluded'
        Arguments:
            args
            kwargs
        """
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

    def area(self):
        """
        Thi si a function that returns the area value of
        the Rectangle instance
        Return:
            width * height
        """
        return self.width * self.height

    def display(self):
        """
        Display is a that prints in stdout the Rectangle instance
        with the character # - you don’t need to handle x and y here
        """
        for i in range(self.height):
            print("#" * self.width)

    def display(self):
        """
        Display is a that prints in stdout the Rectangle instance
        with the character # - you don’t need to handle x and y here
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    """
    def to_csv_dict(self):
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def from_csv_dict(cls, csv_dict):
        return {"id": int(csv_dict[0]), "width": int(csv_dict[1]),
        "height": int(csv_dict[2]), "x": int(csv_dict[3]),
        "y": int(csv_dict[4])}

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                return [cls.create(**row) for row in reader]
        except FileNotFoundError:
            return []
    """

    def __str__(self):
        """
        This functio is a class Rectangle by overriding
        the __str__ method
        Return:
            f'Rectangle id {x}/{y} - {width}/{height}'
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"
