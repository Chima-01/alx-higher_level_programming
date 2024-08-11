#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id
"""
import sys
import urllib.request


req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    html = response.info()

print(html["X-Request-Id"])
