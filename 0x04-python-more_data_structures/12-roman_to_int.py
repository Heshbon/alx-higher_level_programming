#!/usr/bin/python3
def roman_to_int(roman_string):
    # converts a Roman numeral to an integer
    if not roman_string or type(roman_string) != str:
        return 0
    p = 0
    string = roman_string + ' '
    for a in range(len(string)):
        if string[a] == 'I':
            if string[a + 1] == 'V' or string[a + 1] == 'X':
                p -= 1
            else:
                p += 1
        elif string[a] == 'V':
            p += 5
        elif string[a] == 'X':
            if string[a + 1] == 'L' or string[a + 1] == 'C':
                p -= 10
            else:
                p += 10
        elif string[a] == 'L':
            p += 50
        elif string[a] == 'C':
            if string[a + 1] == 'D' or string[a + 1] == 'M':
                p -= 100
            else:
                p += 100
        elif string[a] == 'D':
            p += 500
        elif string[a] == 'M':
            p += 1000
    return p
