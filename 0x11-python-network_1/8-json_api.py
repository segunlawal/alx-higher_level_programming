#!/usr/bin/python3
"""Python script that takes in a letter and sends a
POST request with the letter as a parameter"""

import requests
import sys


if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    value = {"q": q}

    r = requests.post(url, data=value)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
