#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialisation of student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved otherwise retrieve all
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__

        my_name = dict()

        for key, a in self.__dict__.items():
            if key in attrs:
                my_name[key] = a
        return my_name

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, a in json.items():
            if hasattr(self, key):
                setattr(self, key, a)
