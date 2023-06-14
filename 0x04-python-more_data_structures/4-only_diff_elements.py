#!/usr/bin/python3

# This function that returns a set of all elements
# present in only one set.

def only_diff_elements(set_1, set_2):

    element = []

    for i in set_1:
        if i not in set_2:
            element.append(i)
        else:
            for item in set_2:
                if item not in set_1:
                    element.append(item)

    return element
