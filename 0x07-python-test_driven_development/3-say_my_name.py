#!/usr/bin/python3
"""
function that prints the full name of an individual
"""


def say_my_name(first_name, last_name=""):
    """
    prints first_name and last_name to stdout
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
