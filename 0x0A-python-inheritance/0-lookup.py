#!/usr/bin/python3
"""defines attributes lookup function"""


def lookup(obj):
    """returns attributes
        Args:
            obj: object
        Return:
            list: list attributes
    """
    return dir(obj)
