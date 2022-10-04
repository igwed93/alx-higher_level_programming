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
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
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
        """returns the json rep of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes an object to a
            textfile using json string
        Args:
            list_objs - objects to convert
            cls - filename
        """
        if cls is None:
            return
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))


if __name__ == "__main__":
    Base()
