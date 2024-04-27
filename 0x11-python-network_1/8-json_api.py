#!/usr/bin/python3
"""Python script that takes in a letter
  - Sends a POST request to http://0.0.0.0:5000/search_user"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    item = {"q": q}

    req = requests.post("http://0.0.0.0:5000/search_user", data=item)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
