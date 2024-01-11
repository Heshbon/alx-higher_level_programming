#!/usr/bin/python3
"""defines the inherit from module"""


def inherits_from(obj, a_class):
    """check if the object is an instance of a class that inherited"""
    return isinstance(obj, a_class) and type(obj) != a_class
