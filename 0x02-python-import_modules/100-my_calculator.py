#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import sub, mul, div, add

    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py\
 <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]

        if operator:
            if operator == '+':
                print("{:d} + {:d} = {:d}".format(
                    a, b, add(a, b)))
            elif operator == '-':
                print("{:d} - {:d} = {:d}".format(
                    a, b, sub(a, b)))
            elif operator == '*':
                print("{:d} * {:d} = {:d}".format(
                    a, b, mul(a, b)))
            elif operator == '/':
                print("{:d} / {:d} = {:d}".format(
                    a, b, div(a, b)))
            else:
                print("Unknown operator. Available operators:\
 +, -, * and /")
                exit(1)
