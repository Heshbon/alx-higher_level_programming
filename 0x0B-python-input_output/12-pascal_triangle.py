#!/usr/bin/python3
"""function def pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = []

    for a in range(n):
        row = []
        for b in range(a + 1):
            if b == 0 or b == a:
                row.append(1)
            else:
                prev_row = triangle[a - 1]
                row.append(prev_row[b - 1] + prev_row[b])
        triangle.append(row)
    return (triangle)
