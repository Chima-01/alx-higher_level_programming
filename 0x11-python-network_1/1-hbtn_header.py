#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and
    displays the value of the X-Request-Id
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        html = response.headers
        print(html.get("X-Request-Id"))
