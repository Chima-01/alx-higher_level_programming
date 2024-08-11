#!/usr/bin/python3
"""
     Python script that takes in a URL, sends a request to the URL
     and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        response = urlopen(req)
        print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
