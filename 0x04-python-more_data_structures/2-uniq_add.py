#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueList  = set(my_list)
    sum = 0

    for e in uniqueList:
        sum += e
    return sum
