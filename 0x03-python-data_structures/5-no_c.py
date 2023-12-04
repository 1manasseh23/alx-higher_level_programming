#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for glk in my_string:
        if glk != "c" and glk != "C":
            new_str = new_str + glk
    return new_str
