#!/usr/bin/python3
"""
This is a class Student that defines a student
by based on 9-student.py
"""


class Student:
    """
    Instantiation with first_name, last_name and age
    Arguments:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    """
    Public method that retrieve a dictionary representation
    of a Student instance (same as 8-class_to_json.py
    Arguments:
        attrs
    """
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
