#!/usr/bin/python3
"""Python script that fetches URL using `requests` and
displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    html = requests.get(url)

    print("{}".format(html.headers.get("X-Request-Id")))
