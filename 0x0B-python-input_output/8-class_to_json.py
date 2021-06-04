#!/usr/bin/python3
""" A function that returns the dictionary description with
simple data structure for JSON serialization of an object """


def class_to_json(obj):
    """ Returns the dictionary description """
    return obj.__dict__
