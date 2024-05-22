#!/usr/bin/python3
"""Defines a subclass square rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initialize a new square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method to be implemented"""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
