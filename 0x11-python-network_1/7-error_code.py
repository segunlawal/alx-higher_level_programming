#!/usr/bin/python3
"""Python script that fetches URL and handles exceptions"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code == 200:
        print(r.text)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
