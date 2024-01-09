#!/usr/bin/python3
"""
Module in Python that provides methods
for working with JSON data
"""


import sys
import json
from typing import List

def save_to_json_file(my_obj: List, filename: str) -> None:
    """
    Write an object to a file using JSON representation
    Argument:
        my_obj
        filename
    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename: str) -> List:
    """
    Read a JSON file and returns the coresponding object
    Argument:
        filename
        mode
        encoding
    Returns:
        The object represented by the JSON data in the file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == '__main__':
    filename = 'add_item.json'
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)

    print(load_from_json_file(filename))
