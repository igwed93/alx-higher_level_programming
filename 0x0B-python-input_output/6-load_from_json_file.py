#!/usr/bin/python3
""" module contains function function that creates
    an Object from a “JSON file"
"""
import json



def load_from_json_file(filename):
    """creates an object from a JSON file
    Args:
        filename
    """
    if filename is None:
        return
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
