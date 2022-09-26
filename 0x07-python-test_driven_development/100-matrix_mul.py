#!/usr/bin/python3
"""
defines function that multiiplies any two matrix.

NB: the number of columns in the first matrix must be equal to the number
of rows in the second matrix.
"""


def matrix_mul(m_a, m_b):
    """
    multiplies two matrix
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not (isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if not (isinstance(m_b, list)):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):  # no of rows in matrix a
        new_row = []
        for j in range(len(m_b[0])):  # no of columns in matrix b
            prod = 0
            for k in range(len(m_b)):  # no of rows in matrix b
                prod += m_a[i][k] * m_b[k][j]
            new_row.append(prod)
        new_matrix.append(new_row)

    return (new_matrix)
