#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    maximum = my_list[0]
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[i]:
                maximum = my_list[j]
                return (maximum)
    return maximum
