#!/usr/bin/env python3
def no_c(my_string):
    new = []
    for a in my_string:
        if a != 'c' and a != 'C':
            new.append(a)
    return ''.join(new)
