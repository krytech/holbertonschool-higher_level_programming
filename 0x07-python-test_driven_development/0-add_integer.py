#!/usr/bin/python3
"""
This is a comment about a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    This is a comment about a function that returns a + b
    after checking if the values are integers or floats
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
