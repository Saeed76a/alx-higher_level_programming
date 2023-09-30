#!/usr/bin/python3
"""hard coding is a hard working"""
import requests
import sys

if __name__ == '__main__':
    me = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(str(me.text))
