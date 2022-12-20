#!/usr/bin/python3

"""
takes in a URL and an email, sends a POST request to it with the email as a
parameter, and displays the response body decoded in utf-8
Usage: ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
