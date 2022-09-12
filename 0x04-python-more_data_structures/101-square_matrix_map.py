#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    # x = row, and y = column
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
