#!/usr/bin/python3
"""
Module in Python that provides methods
for working with JSON data
"""


import json


def load_from_json_file(filename):
    """
    This is a function that creates an Object from a “JSON file”
    Argument:
        filename
        mode
        encoding
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
