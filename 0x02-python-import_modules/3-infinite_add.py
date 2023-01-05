#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
summ = 0
for i in range(argc):
    if i == 0:
        continue
    summ = summ + int(argv[i])
print("{:d}".format(summ))
