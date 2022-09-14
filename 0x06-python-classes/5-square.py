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

    def my_print(self):
        """ Public instance method """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("{}".format("#" * self.__size))


if __name__ == "___main__":
    Square()
