#!/usr/bin/python3

def add_integer(a, b=98):
    """
    add two integers.

    Args:
    a (int): An integer.
    b (int): An integer. Defaults to 98.

    Retuns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
