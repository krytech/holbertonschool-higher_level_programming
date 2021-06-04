#!/usr/bin/python3
""" A function that creates an object from a JSON file """


def load_from_json_file(filename):
    """ Creates an object from a JSON file """
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
