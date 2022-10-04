#!/usr/bin/python3
"""
create a class base that has a private class attribute __nb_objects
and public instance attribute id
"""
import json


class Base:
    """
    Attributes:
        __nb_objects
        id
    Methods:
        __init__()
        to_json_string(list_dictionaries):
    """
    __nb_objects = 0  # public class attribute

    def __init__(self, id=None):
        # if id is given by user, assign id to the value
        if id is not None:
            self.id = id
        else:  # else assign it to an increment of the public class attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the json rep of list_dictionaries'''
        if list_dictionaries is None:
            return "[]"
        elif list_dictionaries == [] or list_dictionaries == [{}]:
            return "[]"
        return json.dumps(list_dictionaries)


if __name__ == "__main__":
    Base()
