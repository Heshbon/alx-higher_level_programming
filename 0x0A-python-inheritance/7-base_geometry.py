#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """Reprsent class geometry"""

    def area(self):
        """Compute area not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
