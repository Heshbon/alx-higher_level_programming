#!/usr/bin/python3
"""defines a student"""


class Student:
    """represents student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        my_attrs = {}
        for a, num in self.__dict__.items():
            my_attrs[a] = num
        return my_attrs
