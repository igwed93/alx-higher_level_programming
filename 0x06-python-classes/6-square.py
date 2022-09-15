#!/usr/bin/python3

"""Define a Class Square"""


class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Private instance attribute """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter for square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for square size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Getter for square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter  for square position"""
        if type(value[0]) and type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Public intance method """
        return self.__size ** 2

    def my_print(self):
        """ Public instance method """
        if self.__size == 0:
            print("")
            return
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                print("{}".format(" " * self.__position[0]), end="")
                print("{}".format("#" * self.__size))


if __name__ == "___main__":
    Square()
