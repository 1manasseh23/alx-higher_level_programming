#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    check_string = ""
    for me in range(len(str)):
        if me != n:
            check_string = check_string + str[me]

    return check_string
