#!/usr/bin/python3
"""
0. Lookup
function:
    that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """
    Create a list of available
    attributes and methods of an object

    Args:
        obj (obj): an object
    Returns:
        the list of available
        attributes and methods of an object
    """
    return dir(obj)
