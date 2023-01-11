#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    unique_num = []

    for num in my_list:
        if num not in unique_num:
            unique_num.append(num)

    for num in unique_num:
        add += num

    return add
