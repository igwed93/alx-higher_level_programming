#!/usr/bin/python3

"""
Script that takes in a URL, sends request to it and displays
the body of the response decoded in utf-8.
HTTPError exceptions are well managed
Usage: ./3-error_code.py http://0.0.0.0:5000
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    import urllib.error
    from sys import argv

    url = argv[1]
    req = Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
