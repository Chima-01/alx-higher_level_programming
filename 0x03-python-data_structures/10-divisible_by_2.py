#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        length = len(my_list)
        bool_list = []

        for i in range(length):
            if my_list[i] % 2 == 0:
                bool_list.insert(i, True)
            else:
                bool_list.insert(i, False)

        return bool_list
