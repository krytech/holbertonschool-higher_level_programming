#!/usr/bin/python3
""" A function that returns the JSON representation of an object """


def to_json_string(my_obj):
    """ Returns the JSON representation of an obj (string) """
    import json
    return json.dumps(my_obj)
