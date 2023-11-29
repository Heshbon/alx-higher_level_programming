#!/usr/bin/python3

def uppercase(str):
    for b in str:
        p = ord(b)
        if (p >= ord('a')) and (p <= ord('z')):
            b = chr(p-ord('a')+ord('A'))
        print("{}".format(b), end='')
    print()
