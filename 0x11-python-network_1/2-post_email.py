#!/usr/bin/python3
import urllib.request
import sys


data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
req = urllib.request.Request(sys.argv[1], data=data, method='POST')
with urllib.request.urlopen(req) as response:
    result = response.read()
print(str(result)[2:-1])
