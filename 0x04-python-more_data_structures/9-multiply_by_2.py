#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for d in dic:
        dic[d] *= 2
    return dic
