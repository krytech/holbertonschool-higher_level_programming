#!/usr/bin/python3
""" A function that returns int lists of a pascal
triangle of any given size n """


def pascal_triangle(n):
    """ Returns a list of ints representing
    Pascal's triangle using n """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n - 1):
        triangle.append([a + b for a, b in zip([0] + triangle[-1],
                         triangle[-1] + [0])])
    return triangle
