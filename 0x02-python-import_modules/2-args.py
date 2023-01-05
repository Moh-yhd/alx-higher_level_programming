#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    else:
        if len(sys.argv) == 1:
            print("{:d} argument.".format(len(sys.argv) - 1))
        else:
            print("{:d} argument:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        j = i + 1
        if j == len(sys.argv):
            break
        print("{:d}: {}".format(j, sys.argv[j]))
