#!/usr/bin/python3
def add_integer(a, b=98):
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    elif isinstance(a, float) is True:
        a = int(a)
    elif isinstance(b, float) is True:
        b = int(b)

    return (a + b)
