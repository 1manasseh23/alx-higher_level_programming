#!/usr/bin/python3
"""
Module in Python that provides methods
for working with JSON data
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This is a function that writes an Object to a text file
    using a JSON representation
    Argument:
        filename
        mode
        encoding
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
