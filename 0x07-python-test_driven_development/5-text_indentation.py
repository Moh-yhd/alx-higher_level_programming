#!/usr/bin/python3
"""
    The "5-text_indentation" module
    The module only has one function: text_indentation

"""


def text_indentation(text):
    """ Prints a text within two lines after ., ?, or : charachters"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    flag = 0
    flag2 = 0
    while i < len(text):
        if flag == 0 and text[i] == ' ':
            i = i + 1
            continue
        if flag2 == 1 and text[i] == ' ':
            i = i + 1
            continue
        print("{}".format(text[i]), end="")
        flag = 1
        flag2 = 0
        if text[i] in ('.', ':', '?'):
            print('\n')
            i = i + 1
            flag2 = 1
        i = i + 1
