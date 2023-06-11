#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if len(my_list) > 0:
        for i in my_list:
            b = a > i
            if b is False:
                a = i
        return a
    return None
