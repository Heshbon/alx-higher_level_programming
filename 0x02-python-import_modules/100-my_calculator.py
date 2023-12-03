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
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif operator == '-':
        result = sub(a, b)
        print("{} - {} = {}".format(a, b, result))
    elif operator == '*':
        result = mul(a, b)
        print("{} * {} = {}".format(a, b, result))
    elif operator == '/':
        result = div(a, b)
        print("{} / {} = {}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
