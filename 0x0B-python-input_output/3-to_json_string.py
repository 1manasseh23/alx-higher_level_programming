#!/usr/bin/python3
"""
Module in Python that provides methods
for working with JSON data
"""


import json


"""
a function that returns the JSON representation
of an object (string)
Argument:
    my_obj
"""


def to_json_string(my_obj):
    """
    Return JSON representation as a string
    """
    return json.dumps(my_obj)
