#!/usr/bin/python3
"""defines a read text file"""


def read_file(filename=""):
    """prints it to stdout"""
    with open(filename, 'r') as f:
        print(f.read(), end='')
