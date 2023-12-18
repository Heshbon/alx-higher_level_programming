#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""
    b = []
    n = 0
    for a in range(list_length):
        try:
            n = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            n = 0
        except ZeroDivisionError:
            print("division by 0")
            n = 0
        except IndexError:
            print("out of range")
            n = 0
        finally:
            b.append(n)
    return b
