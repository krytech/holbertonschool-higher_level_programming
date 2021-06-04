#!/usr/bin/python3
""" Contains a class Student """


class Student:
    """ Defines a class Student """
    def __init__(self, first_name, last_name, age):
        """ Initialize a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a student """
        return self.__dict__
