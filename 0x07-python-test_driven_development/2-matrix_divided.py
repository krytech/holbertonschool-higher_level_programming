#!/usr/bin/python3
"""
A function which divides the values in a matrix by a variable
"""


def matrix_divided(matrix, div):
    """
    Returns a new list with new values from the original list
    divided by the div value
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(err_msg)

    new_matrix = []
    for lists in matrix:
        if type(lists) != list:
            raise TypeError(err_msg)
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for i in lists:
            if type(i) not in (int, float):
                raise TypeError(err_msg)
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)
    return new_matrix
