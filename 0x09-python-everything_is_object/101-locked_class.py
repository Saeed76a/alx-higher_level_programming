#!/usr/bin/python3
"""declare a LockedClass class"""


class LockedClass(object):
    """define a LockedClass class"""
    def __setattr__(self, key, value):
        """initialize a LockedClass class"""
        if not key == "first_name":
            raise AttributeError("'LockedClass' object has no \
                                 attribute '{}'".format(key))
        object.__setattr__(self, key, value)
