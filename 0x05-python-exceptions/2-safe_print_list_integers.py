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
            print("{:d}".format(my_list[i]), end="")
            val += 1
        except (TypeError, ValueError):
            pass
    print()
    return val
