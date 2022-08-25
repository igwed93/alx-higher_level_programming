#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 90:
            print("{:s}".format(chr(ord(i) - 32)), end="")
        else:
            print("{:s}".format(i), end="")
