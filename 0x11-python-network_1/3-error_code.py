#!/usr/bin/python3
"""Python script that fetches URL and handles exceptions"""
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print("{}".format(html.decode("utf-8")))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
