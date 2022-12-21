#!/usr/bin/python3

"""
Python script that takes your GitHub credentials and uses the GitHub API
to display your id.
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    res = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(res.json().get('id'))
