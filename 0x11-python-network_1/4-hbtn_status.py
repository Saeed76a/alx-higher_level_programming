#!/usr/bin/python3
import requests

ayoub = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\
\t- content: {}".format(type(ayoub.text), ayoub.text))
