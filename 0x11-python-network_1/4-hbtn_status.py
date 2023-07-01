#!/usr/bin/python3
"""Python script that fetches URL using `requests`"""

import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    html = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
