#!/usr/bin/python3
"""defines the class square"""


class Square:
    """represents the class square"""

    def __init__(self, size=0):
        """class square initialized"""
        self.size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """the area of the square"""
        return self.__size**2

    def my_print(self):
        """prints the square into stdout"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                print('#'*self.__size)
