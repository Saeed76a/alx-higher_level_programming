#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new += c
    return new
