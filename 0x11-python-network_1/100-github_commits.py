#!/usr/bin/python3
"""
Use Github API to list last 10 commits given a repo name and owner
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()

    for i in range(10):
        print("{}: {}".format(commits[i].get("sha"),
              commits[i].get("commit").get("author").get("name")))
