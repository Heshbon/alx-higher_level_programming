#!/usr/bin/python3
"""defines matrix divide module"""


def matrix_divided(matrix, div):
    """returns a new matrix divided by div"""

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of '
                        'integers/floats')

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of '
                            'integers/floats')
        for colmn in matrix[0]:
            if type(colmn) is not int and type(colmn) is not float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    a = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for colmn in range(len(matrix[0])):
            a[row][colmn] = round(matrix[row][colmn] / div, 2)

    return (a)
