#!/usr/bin/python3
lowercase = ord('z')
uppercase = ord('Z')
printLowerCase = 0
while lowercase >= ord('a') and uppercase >= ord('A'):
    if printLowerCase == 0:
        print("{:s}".format(chr(lowercase)), end="")
    else:
        print("{:s}".format(chr(uppercase)), end="")

    printLowerCase = ~(printLowerCase)
    lowercase -= 1
    uppercase -= 1
