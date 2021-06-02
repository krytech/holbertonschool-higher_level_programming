#!/usr/bin/python3
"""
A function to check if the object is an instance of, or if the object is
an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """ Return: True if object is an instance of class, otherwise False """
    return isinstance(obj, a_class)
