#!/usr/bin/python3
""" module that contains a method that returns an object
    (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string
    Args:
        my_str: json string representation
    Return:
        python object
    """
    if my_str is None:
        return

    return json.loads(my_str)
