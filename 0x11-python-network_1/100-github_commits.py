#!/usr/bin/python3
""" Time for an interview! Challenge """

import requests
import sys

if __name__ == "__main__":
    repName = sys.argv[1]
    ownerName = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        ownerName, repName)
    r = requests.get(url)
    body = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(body[i]["sha"],
                                  body[i]["commit"]["author"]["name"]))
    except:
        pass
