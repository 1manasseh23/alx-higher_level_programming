#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        my_value = int(value)
        print("{:d}".format(my_value))
        return True
    except (ValueError, TypeError):
        print("Exception: Unknown format code 'd' for object of type 'str'",
              file=sys.stderr)
        return False
