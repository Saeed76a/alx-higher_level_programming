#!/usr/bin/python3
"""hard coding is a hard working"""
import requests
import sys

if __name__ == '__main__':
    moi = requests.get(sys.argv[1])
    if moi.status_code >= 400:
        print('Error code: {}'.format(moi.status_code))
    else:
        print(moi.text)
