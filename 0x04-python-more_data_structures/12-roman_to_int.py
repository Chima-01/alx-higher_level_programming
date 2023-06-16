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
                return None

        length = len(roman_val)
        if length % 2 != 0:
            roman_val.append(0)

        diff, value = 0, 0

        for i in range(0, length, 2):
            if roman_val[i] < roman_val[i + 1]:
                diff = roman_val[i + 1] - roman_val[i]
            else:
                diff = roman_val[i] + roman_val[i + 1]
            value += diff

        return value
    else:
        return None
