#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    n = len(sentence)
    c = sentence[0]
    tuple_return = ()
    tuple_return += (n, c)
    return tuple_return
