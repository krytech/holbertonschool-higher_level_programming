#!/usr/bin/python3
""" A function that writes an object to a text file using JSON """


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file in JSON """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
