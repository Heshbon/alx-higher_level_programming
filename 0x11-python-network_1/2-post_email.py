#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter
  - Displays the body of the response (decoded in utf-8)"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    item = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(item).encode("utf-8")

    # Creates a POST request
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
