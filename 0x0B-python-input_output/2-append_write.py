#!/usr/bin/python3
""" A function to append text to file """


def append_write(filename="", text=""):
    """
        Filename: File to append text to
        text: test to apppend to file
    """
    open(filename, "w", encoding="utf-8")

    with open(filename, "a") as f:
        return f.write(text)
