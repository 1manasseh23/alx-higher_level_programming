#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        parsed_value = int(value)
        print("{:d}".format(parsed_value))
        return True
    except (ValueError, TypeError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
