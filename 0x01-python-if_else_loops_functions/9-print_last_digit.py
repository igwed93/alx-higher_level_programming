#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
        ld = number % 10
        print("{:d}".format(-1 *ld), end="")
        return (-1 * ld)
    else:
        print("{:d}".format(number % 10), end="")
        return (number % 10)
