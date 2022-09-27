#!/usr/bin/python3
"""
Contains method is_same_class
returns True if object is exactly an instance of specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    Retrun:
        True if obj is exactly an instance of specified class
    """
    return (isinstance(obj, a_class))
