#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Returns the real number of integers printed"""
    div = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            div += 1
        except (ValueError, TypeError):
            continue
    print()
    return (div)
