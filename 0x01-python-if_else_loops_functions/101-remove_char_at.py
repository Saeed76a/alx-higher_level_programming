#!/usr/bin/python
def remove_char_at(str, n):
    if n < 0:
        return str
    strtot = str[:n]
    strtot += str[n+1:]
    return strtot
