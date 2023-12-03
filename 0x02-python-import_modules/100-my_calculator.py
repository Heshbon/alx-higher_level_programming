#!/usr/bin/python3

import sys
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div
    m = sys.argv
    n = len(m) - 1

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(m[n - 2])
    b = int(m[n])
    operator = m[n - 1]
    result = 0

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
