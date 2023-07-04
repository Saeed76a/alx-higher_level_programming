#!/usr/bin/python3
L = [-1]
def magic_string():
    L[0] += 1
    return ("BestSchool" + (", BestSchool") * L[0])
