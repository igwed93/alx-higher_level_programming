#!/usr/bin/python3
"""Rectangle class module - tests located in tests/test_base.py"""

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle - inherits from Base
        Attributes:
            width - (private)
            height - (private)
            x - (private)
            y - (private)
        Methods:
            __init__(self, width, height, x, y, id)
            width(self)
            width(self, value)
            height(self)
            height(self, value)
            x(self)
            x(self, value)
            y(self)
            y(self, value)
            area(self)
            validate_integer(self, name, value, eq)
            display(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ magic """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_integer(self, name, value, eq=True):
        """validate the value as int that is >= 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """get rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set rectangle width to value """
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """get rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ display rectangle """
        rep = "#" * self.__width
        [print(rep) for i in range(self.__height)]

    def __str__(self):
        """ string rep of rectangle """
        return "[{}] ({}) {}/{} - {}/{}". \
            format(type(self).__name__, self.id, self.x,
                   self.y, self.width, self.height)


if __name__ == "__main__":
    Rectangle()
