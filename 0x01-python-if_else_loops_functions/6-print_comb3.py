#!/usr/bin/python3

for p in range(10):
    for s in range(p + 1, 10):
        if p < s:
            if p == 8:
                print("{}{}".format(p, s))
            else:
                print("{}{}".format(p, s), end=", ")
