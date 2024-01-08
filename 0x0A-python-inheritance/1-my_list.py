#!/usr/bin/python3
"""
This is a function that inherits from list
Attribute:
    list
"""


class MyList(list):
    """
    Print_sorted is function that prints the list
    but sorted (ascending sort)
    Attribute:
        self
    """
    def print_sorted(self):
        print(sorted(self))
