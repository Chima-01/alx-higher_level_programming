#!/usr/bin/python3
"""
    python script that takes in a URL, sends a request to the URL and
    displays the body of the response/ Error code
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
