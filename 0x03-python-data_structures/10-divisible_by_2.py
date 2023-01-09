#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    check = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 != 0:
            check.append(False)
        elif my_list[i] % 2 == 0:
            check.append(True)
        i += 1
    return check
