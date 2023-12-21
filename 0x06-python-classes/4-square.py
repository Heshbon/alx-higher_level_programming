#!/usr/bin/python3
"""defines the class square"""


class Square:
    """represents the class square"""

    def __init__(self, size=0):
        """square initialized"""
        self.size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) != int:
            raise TyepError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

        def area(self):
            """returns the value of the square"""
            return self.__size**2
