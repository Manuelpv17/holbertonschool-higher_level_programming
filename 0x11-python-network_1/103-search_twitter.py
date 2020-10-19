#!/usr/bin/python3
""" Python script that takes in 3 strings and
sends a search request to the Twitter API """

import base64
import requests
import sys

if __name__ == "__main__":
    consumerKey = sys.argv[1]
    consumerSecret = sys.argv[2]

    mix = "{}:{}".format(consumerKey, consumerSecret).encode("ascii")
    encodeKey = base64.b64encode(mix).decode("ascii")

    url = "https://api.twitter.com/oauth2/token?grant_type=client_credentials"
    headers = {
        "Authorization": "Basic {}".format(encodeKey),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    res = requests.post(url, headers=headers)
    access_token = res.json()["access_token"]

    url = "https://api.twitter.com/1.1/search/tweets.json"
    headers = {"Authorization": "Bearer {}".format(access_token)}
    params = {"q": sys.argv[3], "count": "5"}
    resSearch = requests.get(url, headers=headers, params=params)
    try:
        for tweet in resSearch.json()["statuses"]:
            print("[{}] {} by {}".format(tweet["id"],
                                         tweet["text"], tweet["user"]["name"]))
    except:
        pass
