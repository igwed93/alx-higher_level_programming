#!/usr/bin/python3
""" module that contains a function that reads a file to stdout"""


def read_file(filename=""):
    """ reads a file to the stdout stream """
    if not filename:
        return

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
