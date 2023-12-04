#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(None)
    biger = my_list[0]

    for numbs in my_list:
        if numbs > biger:
            biger = numbs
    return(biger)
