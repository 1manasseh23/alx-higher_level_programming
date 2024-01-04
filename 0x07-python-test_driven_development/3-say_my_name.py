#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the user's name.

    Args:
    first_name (str): The user's first name.
    last_name (str): The user's last name . Defaults to an empty string.

    Raise:
    TypeError: If firs_name or last_name is not a string.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
