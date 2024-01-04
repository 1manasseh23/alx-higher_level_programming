#!/usr/bin/python3

def print_square(size):
    """
    This function prints a square with the character #.

    Args:
    - size: an integer representing the size lenngth of the square.

    Raises:
    - TypeError: if size is not an integer.
    - ValueError: if size is less than 0.

    Returns:
    - None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be  >= 0")
    else:
        for i in range(size):
            print("#" * size)
