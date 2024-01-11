#!/usr/bin/python3
"""defines text indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines after these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError('text must be a string')

    a = True
    for c in text:
        if not (a and c == ' '):
            print(c, end='')
            a = False
            if c in '.?:':
                print('\n')
                a = True
