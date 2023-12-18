#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for j in range(x):
            print(my_list[j], end="")
            counter += 1
        return counter
    except IndexError:
        return counter
    finally:
        print("")
