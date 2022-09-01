#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = []
    for key in a_dictionary:
        d.append(key)

    for k in sorted(d):
        print("{:s}".format(k), end=": ")
        print(a_dictionary.get(k))

