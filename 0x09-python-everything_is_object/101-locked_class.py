#!/usr/bin/python3
class LockedClass(object):
    def __setattr__(self, key, value):
        if not key == "first_name":
            raise AttributeError("'LockedClass' object has no \
                                 attribute '{}'".format(key))
        object.__setattr__(self, key, value)
