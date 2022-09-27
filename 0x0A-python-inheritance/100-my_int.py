#!/usr/bin/python3

"""
contains class that inherists from int
NB: has == and != operators inverted!
"""


class MyInt(int):
    """
    Methods:
    __init__(self, num)
    __eq__(self, other)
    __ne__(self, other)
    """
    def __init__(self, val):
       """ initialize val """
       self.val = val

    def __eq__(self, other):
        """
        Return:
            True if both not equal
        """
        return self.val != other

    def __ne__(self, other):
        """
        Return:
            True if both are equal
        """
        return self.val == other
