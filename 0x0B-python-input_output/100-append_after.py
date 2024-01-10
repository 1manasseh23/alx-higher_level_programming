#!/usr/bin/python3
"""
This is a function that inserts a line of text to a file
after each line containing a specific string
Arguments:
    filename
    search_string
    new_string
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
