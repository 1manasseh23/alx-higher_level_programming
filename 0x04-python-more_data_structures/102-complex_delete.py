#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {me: my for me, my in a_dictionary.items() if my != value}
