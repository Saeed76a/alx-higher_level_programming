#!/usr/bin/python3
i = [-1]
def magic_string():
    i[0] += 1
    return ("BestSchool" + (", BestSchool") * i[0])
