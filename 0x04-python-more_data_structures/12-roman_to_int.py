#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string:

        roman_num = {
                'M': 1000,
                'D': 500,
                'C': 100,
                'L': 50,
                'X': 10,
                'V': 5,
                'I': 1
                }

        roman_val = []
        for key in roman_string:
            if roman_num[key]:
                roman_val.append(roman_num[key])
            else:
                return 0

        length = len(roman_val)
        roman_val.append(0)

        value = 0

        for i in range(length):
            if roman_val[i] < roman_val[i + 1]:
                value -= roman_val[i]
            else:
                value += roman_val[i]

        return value

    elif not isinstance(roman_string, str):
        return 0
    else:
        return 0
