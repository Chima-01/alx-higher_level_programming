#!/usr/bin/python3
def remove_char_at(str, n):
    strlen = len(str)
    new_str = ""
    for i in range(0, strlen):
        if i != n:
            new_str += str[i]
    return new_str
