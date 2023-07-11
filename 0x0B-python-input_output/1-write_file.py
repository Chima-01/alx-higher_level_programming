#!/usr/bin/python3
"""" This function writes to a file """


def write_file(filename="", text=""):
    """ Args:
            filename: file name to write in
            text: text to write to filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        rite = str(text)
        return f.write(rite)
