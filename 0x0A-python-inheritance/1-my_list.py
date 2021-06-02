#!/usr/bin/python3
"""
A class called MyList
Public instance method that prints the sorted list
"""


class MyList(list):
    """ Inherits from list """
    def print_sorted(self):
        """ Prints a sorted list of ints """
        print(sorted(self))
