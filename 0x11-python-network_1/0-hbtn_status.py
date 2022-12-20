#!/usr/bin/python3

"""
this module fetches https://alx-intranet.hbtn.io/status and
displays the body of the response.
Usage: ./0-hbtn_status.py | cat -e
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
