#!/usr/bin/python3
"""hard coding is a hard working"""
import urllib.request
import sys

if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
    print(str(result)[2:-1])
