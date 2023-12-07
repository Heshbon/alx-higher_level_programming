#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    for a in range(len(my_string)):
        if (my_string[a] != 'c') and (my_string[a] != 'C'):
            result += my_string[a]
    return result
