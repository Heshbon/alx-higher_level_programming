#!/usr/bin/env python3
def no_c(my_string):
    my_copy = [a for a in my_string if a != 'c' and a != 'C']
    return ("".join(my_copy))
