#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        MAX = 0
        for n in my_list:
            if n > MAX:
                MAX = n
        return MAX
    return None
