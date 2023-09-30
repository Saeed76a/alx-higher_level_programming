#!/usr/bin/python3
"""hard coding is a hard working"""
import urllib.request
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
        print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
