#!/usr/bin/python3

"""
script that takes two arguments (repo and owner), and list last 10 commits
usage: ./100-github_commits.py [github_repo] [github_owner]
"""


from sys import argv
import requests


if __name__ == "___main__":
    url = "https://api.github.com/repos/{}/{}/commits/".format(
        argv[2], argv[1])

    r = requests.get(url)
    commits = r.json()
    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
