#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
if argc > 2:
    print("{:d} arguments:".format((argc) - 1))
else:
    if argc == 1:
        print("{:d} argument.".format((argc) - 1))
    else:
        print("{:d} argument:".format((argc) - 1))
for i in range(argc):
    j = i + 1
    if j == argc:
        break
    print("{:d}: {}".format(j, argv[j]))
