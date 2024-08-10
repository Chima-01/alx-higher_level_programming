#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ check if list is empty """
    if not list_of_integers:
        return None
    left, right = 0, (len(list_of_integers) - 1)
    li = list_of_integers

    while (left < right):
        mid = (left + right) // 2

        if li[mid] < li[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return li[left]
