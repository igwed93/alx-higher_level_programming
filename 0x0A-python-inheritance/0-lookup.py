#!/usr/bin/python3
"""
module that looks up the list of available atrributes and methods
of an object
"""


def lookup(obj):
    """
    function that returns the list of attributes and methods
    in an object
    """
    return (list(dir(obj)))
