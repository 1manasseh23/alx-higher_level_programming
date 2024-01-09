#!/usr/bin/python3

def class_to_json(obj):
    """
    This is a function that returns the dictionary description
    with simple data structure list, dictionary, string,
    integer and boolean for JSON serialization of an object
    Argument:
        obj
    Returns:
        A diictonary representation of the object that
        can be converted to JSON
    """
    return obj.__dict__
