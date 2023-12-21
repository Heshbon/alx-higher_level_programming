#!/usr/bin/python3
"""defines the class square"""


class Square:
    """represents the class square"""

    def __init__(self, size=0, position=(0, 0)):
        """square initialized"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """retrieve the current square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the position"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
           or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """the area of the square"""
        return self.__size**2

    def my_print(self):
        """prints the square into stdout"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for a in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
