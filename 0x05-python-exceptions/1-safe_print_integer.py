#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        return False
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except Exception:
        return False
