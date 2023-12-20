0x06. Python - Classes and Objects


In this project, I started by practicing object-oriented programing using classes and objects in Python. I learned about attributes, methods and etc


0. My first square

0-square.py: Python class Square that defines a square

1. Square with size

1-square.py: Python class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size

    Instantiation with size (no type/value verification)


2. Size validation

2-square.py: Python class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size

Instantiation with optional size: def __init__(self, size=0):

    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

    if size is less than 0, raise a ValueError exception with the message size must be >= 0

3. Area of a square

3-square.py: Python class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size

Instantiation with optional size: def __init__(self, size=0)

    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

    if size is less than 0, raise a ValueError exception with the message size must be >= 0

4. Access and update private attribute

4-square.py: Python class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:

    property def size(self): to retrieve it
    property setter def size(self, value): to set it:

5. Printing a square

5-square.py: Python class Square that defines a square by: (based on 4-square.py)

Public instance method: def area(self): that returns the current square area

Public instance method: def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line

6. Coordinates of a square

6-square.py: Python class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
      size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
      if size is less than 0, raise a ValueError exception with the message size must be >= 0
Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
      position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
