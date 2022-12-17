#!/usr/bin/python3

""" module that finds the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """finds the peak value in a list"""
    if list_of_integers == [] or not (isinstance(list_of_integers, list)):
        return (None)
    my_list = list_of_integers[:]
    try:
        my_list.sort()
        length = len(my_list)
    except TypeError:
        return (None)
    return (my_list[length - 1])
