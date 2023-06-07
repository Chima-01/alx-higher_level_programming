#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
           i = i.swapcase()
        print("{:s}".format(i), end="")
    print()
