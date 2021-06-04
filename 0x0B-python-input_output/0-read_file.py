#!/usr/bin/python3
""" A function that reads a text file and prints it to stdout """


def read_file(filename=""):
    """ Reads and prints from the file """
    with open(filename) as f:
        print(f.read(), end="")
