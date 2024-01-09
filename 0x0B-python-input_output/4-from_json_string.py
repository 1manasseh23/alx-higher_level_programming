#!/usr/bin/python3
"""
Module in Python that provides methods
for working with JSON data
"""


import json


"""
This is a function that returns an object
(Python data structure) represented
by a JSON string
Agument:
    my_str
"""


def from_json_string(my_str):
    """
    Return corresponding Python object
    """
    return json.loads(my_str)
