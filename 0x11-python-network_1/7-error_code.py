#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])

    if r.state_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
