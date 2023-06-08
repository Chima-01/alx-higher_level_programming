#!/usr/bin/python3
""" This if statement check if the file script is being
run as the main program"""

if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
