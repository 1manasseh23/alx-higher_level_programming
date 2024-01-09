#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and
returns the number of characters written
Args:
    fileename
"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read())
