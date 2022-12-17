#!/usr/bin/python3

""" find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """finds the peak value in a list"""
    if list_of_integers == [] or not (isinstance(list_of_integers, list)):
        return (None)
    myList = list_of_integers[:]
    first = 0
    last = len(myList) - 1

    if myList[first] > myList[first+1]:
        return myList[first]
    if myList[last] > myList[last-1]:
        return myList[last]

    mid = (first+last)//2
    if myList[mid-1] < myList[mid] and myList[mid+1] < myList[mid]:
        return myList[mid]
    if myList[mid] < myList[mid-1]:
        return find_peak(myList[first:mid+1])
    elif myList[mid] < myList[mid+1]:
        return find_peak(myList[mid:last+1])
    else:
        return myList[first]
