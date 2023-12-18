#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    val = 0
    try:
        iterator = iter(my_list)
        while val < x:
            try:
                value = next(iterator)
                if isinstance(value, int):
                    print("{:d}".format(value), end="")
                    val += 1
            except StopIteration:
                break
        print()
    except TypeError:
        pass
    return val
    """
    val = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                val += 1
        except IndexError:
            break
    print()
    return val
