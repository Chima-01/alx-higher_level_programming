#!/usr/bin/python3

# This function rints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for k, v in sorted(a_dictionary.items()):
            print("{:s}: {}".format(k, v))
