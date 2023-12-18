#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    b = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            b += 1
        except IndexError:
            break
    print("")
    return (b)
