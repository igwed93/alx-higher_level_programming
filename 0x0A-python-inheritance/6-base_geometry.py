#!/usr/bin/python3
""" module contains an empty class """


class BaseGeometry(object):
    """ BaseGeometry class
        method:
            area()
    """
    def area(self):
        """ does nothing but raises an exception """
        raise Exception("area() is not implemented")
