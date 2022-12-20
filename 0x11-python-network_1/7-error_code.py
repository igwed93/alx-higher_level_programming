#!/usr/bin/python3

"""
takes in a URL and an email, sends a request to it, and displays
the response body. status codes >= 400 must be printed
Usage: ./7-error_code.py http://0.0.0.0:5000
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {:d}".format(r.status_code))
    else:
        print(r.text)
