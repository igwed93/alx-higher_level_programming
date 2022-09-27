#!/usr/bin/python3
""" module contains a class """


class BaseGeometry(object):
    """ BaseGeometry class
        method:
            area()
            integer_validator()
    """
    def area(self):
        """ does nothing but raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
