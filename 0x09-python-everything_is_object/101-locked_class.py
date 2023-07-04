#!/usr/bin/python3
"""declare a LockedClass class"""


class LockedClass(object):
    """define a LockedClass class"""
    def __setattr__(self, key, value):
        """initialize a LockedClass class"""
        if not key == "first_name":
            raise AttributeError("'{}' object has no \
                                 attribute '{}'\
                                 ".format(self.__class__.__name__, key))
        object.__setattr__(self, key, value)
