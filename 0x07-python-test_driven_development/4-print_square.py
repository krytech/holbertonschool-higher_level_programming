#!/usr/bin/python3
"""
A function that prints a square with the character #
"""


def print_square(size):
    """
    Prints a suqare with '#' using the size variable
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
