#!/usr/bin/python3
"""defines the class square"""


class Square:
    """represnts the class square"""

    def __init__(self, size=0):
        """the square is initialized"""

        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """the area of the square"""
        return self.__size**2
