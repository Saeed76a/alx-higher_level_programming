#!/usr/bin/python3
"""give me requist id baliz"""
import requests
import sys

if __name__ == '__main__':
    omar = requests.get(sys.argv[1])
    print(omar.headers.get('X-Request-Id'))
