#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
  - Displays the value of the variable X-Request-Id"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    resp = requests.get(url)
    print(resp.headers.get("X-Request-Id"))
