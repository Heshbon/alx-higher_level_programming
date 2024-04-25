#!/usr/bin/python3
"""Python  function that finds a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    # initialize start and start indices
    start, end = 0, len(list_of_integers) - 1

    # Binary search loop
    while start < end:
        # calculate the middle index
        middle = (start + end) // 2
        # determine if the current value is greater than the next value
        if list_of_integers[middle] > list_of_integers[middle + 1]:
            # if true, update end to middle
            end = middle
        else:
            # if false, update start to middle
            start = middle + 1

    # Complexity: O(log(n))
    return list_of_integers[start]
