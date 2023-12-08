#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # prints a dictionary by ordered keys
    for a in sorted(a_dictionary):
        print("{}: {}".format(a, a_dictionary[a]))
