#!/usr/bin/python3
import os
""" A function to read from a file"""


def read_file(filename=""):
    """ Args:
            filename: File to read
    """
    with open(filename, encoding="utf-8") as f:
        file_v = f.read()
        print(file_v, end="")
