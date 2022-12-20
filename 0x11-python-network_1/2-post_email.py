#!/usr/bin/python3

"""
takes in a URL and an email, sends a POST request to it with the email as a
parameter, and displays the response body decoded in utf-8
Usage: ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    import urllib.parse
    from sys import argv

    url = argv[1]
    email = argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
