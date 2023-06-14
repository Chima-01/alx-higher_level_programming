#!/usr/bin/python3

def common_elements(set_1, set_2):

    common_element = [i for i in set_1 for y in set_2 if i == y]

    return common_element
