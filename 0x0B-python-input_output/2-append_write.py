#!/usr/bin/python3
"""
This is a function that appends a string at the end of a
text file (UTF8) and returns the number of characters added
Argument:
    filename
    text
"""


def append_write(filename="", text=""):
    """
    This return appended text to the end of file specified
    by filename and the number of character added
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
