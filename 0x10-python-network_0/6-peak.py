#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ returns a peak from a list of unsorted integers """
    if list_of_integers:
        list_of_integers.sort()
        l = len(list_of_integers)
        return(list_of_integers[l - 1])
    else:
        return (None)
