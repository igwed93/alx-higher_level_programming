#!/usr/bin/python3

"""
takes in a URL, sends a request to it and displays the value of
the X-Request-Id variable
Usage: ./5-hbtn_header.py https://alx-intranet.hbtn.io
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    print(res.headers['X-Request-Id'])
