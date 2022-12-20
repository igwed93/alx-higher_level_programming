#!/usr/bin/python3

"""
takes in a URL, sends a request to it and displays the value of
the X-Request-Id variable
Usage: ./1-hbtn_header.py https://alx-intranet.hbtn.io
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv

    url = argv[1]
    req = Request(url)
    with urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
