#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents a class square"""

    def __init__(self, size=0):
        """the class is initialized"""

        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """returns the value of the square"""
        return self.__size**2
