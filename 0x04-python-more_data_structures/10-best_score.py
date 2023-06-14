#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        n = 0
        for k in a_dictionary:
            if a_dictionary[k] >= n:
                n = a_dictionary[k]
                name = k
        return name
    return None
