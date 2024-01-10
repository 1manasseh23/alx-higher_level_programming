#!/usr/bin/python3
"""
This is a class Student that defines a student by
based on 10-student.py
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
    Public method that retrieves a dictionary representation of
    a Student instance same as 8-class_to_json.py
    Arguments:
        attrs
    """
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: gettr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    """
    Public method that replaces all attributes of the Student instance
    Aguments:
        json
    """
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
