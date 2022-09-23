#!/usr/bin/python3
"""
defines a function that prints two lines after '.', '?', or a ':'
in a string
"""


def text_indentation(text):
    """
    prints a delimeted text
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    new_text = "\n".join(list_lines)
    print(new_text, end="")
