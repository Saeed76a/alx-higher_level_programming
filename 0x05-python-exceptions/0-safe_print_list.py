#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    class outOfRange(Exception):
        def __init__(self, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)
    try:
        i = 0
        for num in my_list:
            print(num, end='')
            i += 1
            if i == x:
                break
        print()
        if i != x:
            raise outOfRange
        else:
            return x
    except outOfRange:
        return i
