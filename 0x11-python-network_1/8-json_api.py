#!/usr/bin/python3
""" Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as
a parameter."""

import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        payload = {"q": ""}
    else:
        payload = {"q": sys.argv[1]}
    res = requests.post("http://0.0.0.0:5000/search_user",
                        data=payload)
    try:
        body = res.json()
        if body == {}:
            print("No result")
        else:
            print("[{}] {}".format(body["id"], body["name"]))
    except:
        print("Not a valid JSON")
