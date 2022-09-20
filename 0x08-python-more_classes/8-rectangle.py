#!/usr/bin/python3

"""
Define a class Rectangle with private attribute width and height,
and public area and perimeter methods, and allows printing using any given
symbol and deletes, and has a public attribute to keep track of number of
instances, and has static method that returns the bigger rectangle out of
two given.
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height
    and public attribute number_of_instances
    Note:
        Area = width * height
        Perimeter = 2 *(width + height)
    Args:
        width (int): width
        height (int): height
    Attributes:
        number_of_instances (int): number_of_instances
        print_symbol (str): print_symbol
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
        bigger_or_equal(rect_1, rect_2)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ private instance attribute """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """ Return width * height """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return 2*(width + height) or (0 if width or height is 0) """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ string representation of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        r = "\n".join([str(self.print_symbol) * self.__width
                      for rows in range(self.__height)])
        return r

    def __repr__(self):
        """ string representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ deletes an instance of Rectangle """
        print("{:s}...".format("Bye rectangle"))
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2


if __name__ == "__main__":
    Rectangle()
