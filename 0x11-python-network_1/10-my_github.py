#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the
GitHub API to display your 'id'.
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get("id"))
