#!/usr/bin/python3

"""define a class MyList"""

class MyList(list):
    """ MyList class
        inherits from the list class
    """
    def print_sorted(self):
        """ prints the sorted list int objects in ascending order """
        print(sorted(self))
