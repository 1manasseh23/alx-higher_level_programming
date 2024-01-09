#!/usr/bin/python3
"""
This is a function that writes a string to a text
file (UTF8) and returns the number of characters written
Argument:
    fileename
"""


def read_file(filename=""):
    """
    Read_file its read the contain of a file
    and print it to the consol
    """
    with open(filename, 'r') as f:
        print(f.read())
