#!/usr/bin/python3
""" A function to append text to file """


def append_write(filename="", text=""):
    """
        Filename: File to append text to
        text: test to apppend to file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
