#!/usr/bin/python3

"""Define a Rectangle Class"""


class Rectangle:
    """ An empty Rectangle Class """
    def __init__(self, width=0, height=0):
        """ private instance attribute """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ property getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ property setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property setter """
        return self.__height

    @height.setter
    def height(self, value):
        """ property setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


if __name__ == "__main__":
    Rectangle()
