#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list:
        length = len(my_list)

        if idx < 0 or idx >= length:
            return my_list

        listcpy = my_list.copy()

        for i in listcpy:
            if listcpy.index(i) == idx:
                listcpy[idx] = element

        return listcpy
