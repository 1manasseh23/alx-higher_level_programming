#!/usr/bin/python3
"""
This is a function that writes a string to a text
file (UTF8) and returns the number of
characters written
Argument:
    filename
    text
"""


def write_file(filename="", text=""):
    """
    Its print the number of character to the consol
    """
    with open(filename, 'w') as f:
        return f.write(text)
