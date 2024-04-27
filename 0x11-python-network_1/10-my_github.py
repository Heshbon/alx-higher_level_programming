#!/usr/bin/python3
"""Python script that takes my GitHub credentials (username and password)
  - Ues the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    resp = requests.get(url, auth=(username, password))
    if resp.status_code == 200:
        print(resp.json().get("id"))
    else:
        print("None")
