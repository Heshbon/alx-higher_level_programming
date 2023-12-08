#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    #  returns a new dictionary with all values multiplied by 2
    new_dictionary = {}
    for a in a_dictionary:
        new_dictionary[a] = a_dictionary[a] * 2
    return new_dictionary
