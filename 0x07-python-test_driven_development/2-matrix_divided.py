#!/usr/bin/python3
def matrix_divided(matrix, div):
    for row in matrix:
        for e in row:
            if not (isinstance(e, int) or isinstance(e, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("div must be a number")

    result = []

    for row in matrix:
        r = []
        for e in row:
            r.append(round((e/div), 2))
        result.append(r)

    return result
