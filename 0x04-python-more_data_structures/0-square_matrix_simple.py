#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Finds the square value of all integers of a matrix
    return ([list(map(lambda a: a * a, row)) for row in matrix])
