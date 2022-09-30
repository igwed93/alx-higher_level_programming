#!/usr/bin/python3
"""This module defines a function called pascal_triangle"""


def pascal_triangle(n):
    """pascal triangle
    Args:
        n: integer term
    returns:
        empty list [] if n <= 0, otherwise,
        a list containing the corresponding
        pascal triangle of the given number
    """
    if type(n) != int:
        return

    if n <= 0:
        return []

    triangle = [[1]]

    for line in range(n - 1):
        series = [1]
        for t in range(line):
            series.append(triangle[line][t] + triangle[line][t + 1])

        series.append(1)
        triangle.append(series)
    return (triangle)
