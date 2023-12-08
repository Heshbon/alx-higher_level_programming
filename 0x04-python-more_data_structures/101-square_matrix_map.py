#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda b: list(map(lambda p: p**2, b)), matrix))
