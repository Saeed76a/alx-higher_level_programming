#!/usr/bin/python3
def uppercase(str):
    strtot = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            strtot += chr(ord(c) - 32)
        else:
            strtot += c
    print('{}'.format(strtot))
