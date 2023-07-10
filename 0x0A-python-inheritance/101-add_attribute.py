#!/usr/bin/python3
"""
13. Can I?
"""


def add_attribute(object, attr, value):
    """
    function:
        adds a new attribute
        to an object if it's possible
    Args:
        object (obj): the object
        attr (str): the attribute
        value (...): the value of the attribute
    Raise:
        TypeError exception, with a message
    """
    if hasattr(object, '__dict__'):
        setattr(object, attr, value)
    else:
        raise TypeError("can't add new attribute")
