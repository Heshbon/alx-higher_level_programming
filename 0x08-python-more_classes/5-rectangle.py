#!/usr/bin/python3
"""defines class rectangle"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.width = width
        self.height = height

    def __del__(self):
        """deletes a rectangle"""
        print('Bye rectangle...')

    def __str__(self):
        """prints rectangle"""
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        for _ in range(self.height):
            string += '#' * self.width + '\n'
        return string.rstrip('\n')

    def __repr__(self):
        """return a string representation of the rectangle"""
        return f'Rectangle({self.width}, {self.height})'

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
