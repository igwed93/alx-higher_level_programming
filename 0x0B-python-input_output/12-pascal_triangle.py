#!/usr/bin/python3
"""This module defines a function called pascal_triangle"""


def pascal_triangle(n):
    """pascal triangle
    Args:
        n: integer term
    returns:
        a list containing the corresponding
        pascal triangle of the given number
    """
    if type(n) != int:
        return
    triangle = []
    if n <= 0:
        return triangle
    series = []
    for i in range(n):
        series = comb(i)
        triangle.append(series)
    return (triangle)



def comb(r):
    """finds the combination of r
    Args: r
    Returns:
        A list containing the combination
        of r
    """
    if type(r) != int:
        return
    com = []

    for j in range(r+1):
        c = int(factorial(r) / (factorial(j) * factorial(r-j)))
        com.append(c)
    return com

def factorial(n):
    """finds the factorial of n
        Args: n
        Returns: n!
    """
    if type(n) != int:
        return
    if n == 0:
        return 1
    return n * factorial(n-1)
