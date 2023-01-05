#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
argc = len(argv)
if argc < 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if argv[2] != '+' and argv[2] != '-' and argv[2] != '/' and argv[2] != '*':
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
if argv[2] == '+':
    result = add(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(int(argv[1]), argv[2], int(argv[3]), result))
if argv[2] == '-':
    result = sub(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(int(argv[1]), argv[2], int(argv[3]), result))
if argv[2] == '*':
    result = mul(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(int(argv[1]), argv[2], int(argv[3]), result))
if argv[2] == '/':
    result = div(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(int(argv[1]), argv[2], int(argv[3]), result))
