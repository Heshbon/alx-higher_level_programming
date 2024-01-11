#!/usr/bin/python3
"""defines inheritted class mylist"""


class MyList(list):
    """implements sorted list class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
