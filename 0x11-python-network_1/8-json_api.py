#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) < 2 else argv[1]
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
