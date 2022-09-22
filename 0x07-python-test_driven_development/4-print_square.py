#!/usr/bin/python3
"""
function that prints a square using #'s to the stdout
"""


def print_square(size):
    """
    prints a square with #'s
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float):
        raise ValueError("size must be an integer")

    if size == 0:
        print("", end="")
    for rows in range(size):
        [print("#", end="") for i in range(size)]
        print("")
