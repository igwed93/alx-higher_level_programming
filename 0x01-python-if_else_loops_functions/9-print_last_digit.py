#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
        print("{:d}".format(number % 10), end="")
        return (number % 10)
    else:
        print("{:d}".format(number % 10), end="")
        return (number % 10)
