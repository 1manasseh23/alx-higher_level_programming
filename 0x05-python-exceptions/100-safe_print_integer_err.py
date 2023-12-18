#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        parsed_value = int(value)
        print("{:d}".format(parsed_value))
        return True
    # except ValueError:
        # print("Exception: wrong value type", file=sys.stderr)
        # return False
    # except TypeError:
        # print("Exception: wrong type", file=sys.stderr)
        # return False
    except (ValueError, TypeError):
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return False
