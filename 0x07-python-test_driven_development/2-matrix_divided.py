#!/usr/bin/python3
"""
    This function divides all element in a matrix
    divides by the arg passed to div parameter
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists)\
                of integers/floats')
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists)\
                of integers/floats')
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_list = []
    deev = 0

    for row in matrix:
        for i in row:
            deev = round((i / div), 2)
            new_list.append(deev)

    return new_list
