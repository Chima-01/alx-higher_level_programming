#!/usr/bin/python3

# This function returns a new dictionary
# with all values multiplied by 2

def multiply_by_2(a_dictionary):

    dct = a_dictionary.copy()

    for k, v in dct.items():
        dct[k] = v * 2
    return dct
