#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            j = ord(i) - 32
        else:
            j = ord(i)
        print("{}".format(chr(j)), end='')
    print('')
