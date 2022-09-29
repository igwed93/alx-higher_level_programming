#!/usr/bin/python3
"""
this module contains function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a 
        textfile using json string
    Args:
        my_obj
        filename
    """
    if my_obj is None or filename is None:
        return
    
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dumps(my_obj, f)
