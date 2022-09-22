#!/usr/bin/python3
"""
defines a function that divides every element of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with dividends
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix == [[]]:
        raise TypeError(msg)
    elif not isinstance(matrix, list):
        raise TypeError(msg)
    else:
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError(msg)

    for row in matrix:
        for e in row:
            if not (isinstance(e, int) or isinstance(e, float)):
                raise TypeError(msg)
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []

    for row in matrix:
        r = []
        for e in row:
            r.append(round((e/div), 2))
        result.append(r)

    return result
