#!/usr/bin/python3
"""
module contains function that returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object """
    if not my_obj:
        return
    return json.dumps(my_obj)
