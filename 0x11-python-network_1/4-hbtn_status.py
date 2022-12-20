#!/usr/bin/python3

"""
this module fetches https://alx-intranet.hbtn.io/status and
displays the body of the response.
Usage: ./4-hbtn_status.py | cat -e
"""


if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
