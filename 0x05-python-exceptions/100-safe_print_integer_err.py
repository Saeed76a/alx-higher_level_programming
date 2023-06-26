#!/usr/bin/python3
from sys import exc_info as error, stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(error()[1]), file=stderr)
        return (False)
