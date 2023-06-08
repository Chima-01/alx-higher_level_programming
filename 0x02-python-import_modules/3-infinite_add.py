#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    argc = len(argv)
    if argc == 1:
        print(f"{add:d}")
    else:
        for i in range(1, argc):
            add += int(argv[i])
        print(f"{add:d}")
