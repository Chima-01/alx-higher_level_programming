#!/usr/bin/python3
import urllib.request
""" Script that fetches https://alx-intranet.hbtn.io/status """

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()

print('Body response:\n\t- type: {}'.format(type(status)))
print(f'\t- content: {status}')
print(f'\t- utf8 content: {status.decode("utf-8")}')
