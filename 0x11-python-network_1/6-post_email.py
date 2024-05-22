#!/usr/bin/python3
"""Python script that takes in a URL and an email address
  - sends a POST request, displays body response"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    item = {"email": sys.argv[2]}

    req = requests.post(url, data=item)
    print(req.text)
