#!/usr/bin/python3
"""
    This function prints a square with the character #
    size of square is determined by size parameter
    raise error if size is less than zero or size is a float
"""


def print_square(size):
    if isinstance(size, float) and size == 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
