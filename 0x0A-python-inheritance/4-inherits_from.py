#!/usr/bin/python3
"""
A function that checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """ Return: True if object is an instance of class that it inherits
    from a subclass, otherwise False """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
