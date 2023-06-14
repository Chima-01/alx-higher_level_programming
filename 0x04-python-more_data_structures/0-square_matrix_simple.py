#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    cp_matrix = list(map(lambda x: list(map(lambda i: pow(i, 2), x)), matrix))

    return cp_matrix
