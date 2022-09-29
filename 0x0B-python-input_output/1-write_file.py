#!/usr/bin/python3
"""
this module contains the definition of a function that writes
to a file. It creates the file if it doesn't exist already,
but overwrites it if it already does
"""


def write_file(filename="", text=""):
    """ writes to a file """
    if not filename:
        return
    char_count = 0  # the amount of characters written

    with open(filename, mode="w", encoding="utf-8") as myFile:
        char_count = myFile.write(text)

    return char_count
