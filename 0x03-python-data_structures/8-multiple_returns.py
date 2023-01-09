#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_return = ()
    if len(sentence) == 0:
        tuple_return += (0, None)
    else:
        n = len(sentence)
        c = sentence[0]
        tuple_return += (n, c)
    return tuple_return
