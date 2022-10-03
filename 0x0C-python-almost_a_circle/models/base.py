#!/usr/bin/python3
"""
create a class base that has a private class attribute __nb_objects
and public instance attribute id
"""


class Base:
    """
    Attributes:
        __nb_objects
        id
    Methods:
        __init__()
    """
    __nb_objects = 0  # public class attribute

    def __init__(self, id=None):
        # if id is given by user, assign id to the value
        if id is not None:
            self.id = id
        else:  # else assign it to an increment of the public class attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


if __name__ == "__main__":
    Base()
