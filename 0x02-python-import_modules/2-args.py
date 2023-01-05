#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) > 2:
        print("{:d} arguments:".format(len(argv) - 1))
    else:
        if len(argv) == 1:
            print("{:d} argument.".format(len(argv) - 1))
        else:
            print("{:d} argument:".format(len(argv) - 1))
    for i in range(len(argv)):
        j = i + 1
        if j == len(argv):
            break
        print("{:d}: {}".format(j, argv[j]))
