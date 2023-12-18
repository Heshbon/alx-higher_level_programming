#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the value of the division, otherwise: None"""
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside result: {}".format(division))
    return division
