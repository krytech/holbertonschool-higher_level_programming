#!/usr/bin/python3
"""
A function to test if an object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ Return: True if it is a copy, otherwise Fail if not """
    return type(obj) == a_class
