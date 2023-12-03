#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    n_args = len(argv) - 1

    if n_args == 0:
        print("0 arguments.")
    elif n_args == 1:
        print("1 argument:")
    else:
        print(f"{n_args} arguments:")

    for a in range(n_args):
        print(f"{a + 1}: {argv[a + 1]}")
