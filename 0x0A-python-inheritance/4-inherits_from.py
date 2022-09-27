#!/usr/bin/python3
"""
Contains method inherits_from
"""


def inherits_from(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    Retrun:
        True if obj is an instance of a class that inherited
        (directly or indirectly) from the specified class
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
