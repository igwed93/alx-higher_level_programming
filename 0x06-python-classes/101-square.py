#!/usr/bin/python3

"""Define a Class Square"""


class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Private instance attribute """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter for square size """
        return (self.__size)

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
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter  for square position"""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Area of a square """
        return (self.__size ** 2)

    def my_print(self):
        """ Print the area of a square """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """ print() representation of a Square. """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")


if __name__ == "___main__":
    Square()
