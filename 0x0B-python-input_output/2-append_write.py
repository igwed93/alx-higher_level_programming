#!/usr/bin/python3
"""
module contains a function that appends a string to the end of the textfile
"""


def append_write(filename="", text=""):
    """ appends a string to the end of a textfile """
    if not filename:
        return
    chars = 0  # the number of characters appended

    with open(filename, mode="a", encoding="utf-8") as a_File:
        chars = a_File.write(text)

    return chars
