#!/usr/bin/python3
"""
This is a class Student that defines a student
"""


class Student:
    """
    Instantiation with first_name, last_name and age
    Attribute:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    Public method that retrieves a dictionary representation
    of a Student instance same as 8-class_to_json.py
    """
    def to_json(self):
        """
        Returns:
            A dictionary representstion of the object
            that can be converted to JSON
            """
        return self.__dict__
