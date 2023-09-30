#!/usr/bin/python3
"""give me requist id baliz"""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print(response.headers.get('X-Request-Id'))
