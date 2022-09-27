#!/usr/bin/python3
"""
Contains method is_kind_of_class
returns True if obj is an instance of specified class,
or an instance of a class that inherited from specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    Retrun:
        True if obj is an instance of specified class,
        or an instance of a class that inherited from specified class
    """
    return (isinstance(obj, a_class))
