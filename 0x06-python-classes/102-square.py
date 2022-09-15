#!/usr/bin/python3

"""Define a Class Square"""


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ Private instance attribute """
        self.__size = size

    @property
    def size(self):
        """ property getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ property setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Public intance method """
        return self.__size ** 2

    def __eq__(self, other):
        """ == comparison """
        return self.area() == other.area()

    def __ne__(self, other):
        """ != comparison """
        return self.area() != other.area()

    def __lt__(self, other):
        """ < comparison """
        return self.area() < other.area()

    def __le__(self, other):
        """ <= comparison """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ > comparison """
        return self.area() > other.area()

    def __ge__(self, other):
        """ >= comparison """
        return self.area() >= other.area()


if __name__ == "___main__":
    Square()
