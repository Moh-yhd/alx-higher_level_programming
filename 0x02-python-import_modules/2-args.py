#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        j = i + 1
        if j == len(sys.argv):
            break
        print("{:d}: {}".format(j, sys.argv[j]))
