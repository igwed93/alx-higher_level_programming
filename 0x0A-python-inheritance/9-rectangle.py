#!/usr/bin/python3
"""
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class
        method:
            __init__(self, width, height)
            area(self)
            __str__
    """
    def __init__(self, width, height):
        """ validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ extends parent's empty method and returns area """
        return (self.__width * self.__height)

    def __str__(self):
        """ prints [Rectangle] <width>/<height> """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
