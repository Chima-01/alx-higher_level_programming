#!/usr/bin/python3
""" 
    This fuctions prints a text with 2 new lines
    after each of these characters: ., ? and : 
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = ['.', '?', ':']
    s = ""

    for i in text:
        if i in char:
            s += '\n' * 2
        else:
            s += i

    print("{:s}".format(s))
