#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)

    if length == 1:
        print(f"{0:d} arguments.")
    elif length == 2:
        print(f"{1:d} argument:")
        print(f"{1:d}: {argv[1]:s}")
    else:
        print("{:d} arguments:".format(length - 1))

        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))
