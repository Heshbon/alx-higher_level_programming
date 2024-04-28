# Python - Inheritance.

In this project, I gained knowledge of Python class inheritance. While practicing inheritance, defining classes with multiple base classes, and overriding inherited methods and properties, I became aware of the distinctions between super-class, base-class and sub-classes.

# Tasks 📃

# 0. Lookup

  + <u>[0-lookup.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py)</u>: Python function that returns the list of available attributes and methods of an object.

# 1. My list

  + <u>[1-my_list.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py)</u>: Python class MyList that inherits from list.

  + Public instance method: `def print_sorted(self): that prints the list, in a sorted (ascending sort).`

# 2. Exact same object

  + <u>[2-is_same_class.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/2-is_same_class.py)</u>: Python function that returns True if the object is exactly an instance of the specified class ; otherwise False.

# 3. Same class or inherit from

  + <u>[3-is_kind_of_class.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/3-is_kind_of_class.py)</u>: Python function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

# 4. Only sub class of

  + <u>[4-inherits_from.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/4-inherits_from.py)</u>: Python function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

# 5. Geometry module

  + <u>[5-base_geometry.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/5-base_geometry.py)</u>: An empty class BaseGeometry.

# 6. Improve Geometry

  + <u>[6-base_geometry.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py)</u>: python class BaseGeometry `(based on 5-base_geometry.py)`.

  + Public instance method: def area(self): that raises an Exception with the message area() is not implemented.

# 7. Integer validator

  + <u>[7-base_geometry.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py)</u>: Python class BaseGeometry `(based on 6-base_geometry.py)`.

  + Public instance method: def area(self): that raises an Exception with the message area() is not implemented.

  + Public instance method: `def integer_validator(self, name, value)`: that validates value:

	+ Assumes name is always a string.

	+ If value is not an integer: raise a TypeError exception, with the message `<name>` must be an integer.

	+ If value is less or equal to 0: raise a ValueError exception with the message` <name>` must be greater than 0.

# 8. Rectangle

  + <u>[8-rectangle.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/8-rectangle.py)</u>: Python class Rectangle that inherits from BaseGeometry `(7-base_geometry.py)`.

  + Instantiation with width and height: def __init__(self, width, height):

	+ width and height must be private. No getter or setter.

	+ width and height must be positive integers, validated by integer_validator.

# 9. Full rectangle

  + <u>[9-rectangle.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/9-rectangle.py)</u>: Python class Rectangle that inherits from BaseGeometry `(7-base_geometry.py)(task based on 8-rectangle.py)`.

  + The area() method must be implemented.

  + Print() should print, and str() should return, the following rectangle description: `[Rectangle] <width>/<height>.`

# 10. Square #1

  + <u>[10-square.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/10-square.py)</u>: Python class Square that inherits from Rectangle (9-rectangle.py).

  + Instantiation with size: def __init__(self, size)::

	+ size must be private. No getter or setter.

	+ size must be a positive integer, validated by integer_validator.

# 11. Square #2

  + <u>[11-square.py](https://github.com/Heshbon/alx-higher_level_programming/blob/master/0x0A-python-inheritance/11-square.py)</u>: Python class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

  + The area() method must be implemented.

  + Instantiation with size: def __init__(self, size)::

	+ size must be private. No getter or setter.

	+ size must be a positive integer, validated by integer_validator.
