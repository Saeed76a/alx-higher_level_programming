#!/usr/bin/python3
from sys import exc_info as error, stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception:
        print("Exception: {}".format(error()[1]), file=stderr)
        return None
