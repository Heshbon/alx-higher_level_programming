#!/usr/bin/python3

def best_score(a_dictionary):
    # returns a key with the biggest integer value
    if not a_dictionary:
        return None
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    return keys[values.index(max(values))]
