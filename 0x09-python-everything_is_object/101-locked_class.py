#!/usr/bin/python3
""" Class called LockedClass """


class LockedClass():
    """ Prevents the user from dynamically creating new
    instance attributes except if it's called 'first_name'
    """
    __slots__ = "first_name"
