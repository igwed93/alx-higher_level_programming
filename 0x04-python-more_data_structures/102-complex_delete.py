#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    invalid_keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            invalid_keys.append(i)

    for i in invalid_keys:
        del a_dictionary[i]
    return a_dictionary
