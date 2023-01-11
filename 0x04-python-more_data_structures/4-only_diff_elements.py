#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elem = []
    for i in set_1:
        if i not in set_2:
            diff_elem.append(i)
    for j in set_2:
        if j not in set_1:
            diff_elem.append(j)

    return diff_elem
