#!/usr/bin/python3
"""
This a function that reads a text file (UTF8) and
prints it to stdout
Argument:
    fileename
"""


def read_file(filename=""):
    """
    Read_file its read the contain of a file
    and print it the consol
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
