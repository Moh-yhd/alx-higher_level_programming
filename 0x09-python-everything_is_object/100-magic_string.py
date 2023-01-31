#!/usr/bin/python3
def magic_string():
    magic_string.i, s = (magic_string.__dict__.get('i', 0)) + 1, "BestSchool"
    return s + (magic_string.i - 1) * (", " + s)
