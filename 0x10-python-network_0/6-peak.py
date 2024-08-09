#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    peak = list_of_integers[0]

    for num in list_of_integers:
        if peak < num:
            peak = num

    return peak
