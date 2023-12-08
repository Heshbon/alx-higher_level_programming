#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    return sum(n * p for n, p in my_list) / sum(p for n, p in my_list)
