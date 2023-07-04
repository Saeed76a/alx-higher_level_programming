#!/usr/bin/python3
class LockedClass(object):
    def __setattr__(self, key, value):
        if not key == "first_name":
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, key))
        object.__setattr__(self, key, value)