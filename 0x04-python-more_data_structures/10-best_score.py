#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary is not None:
        maximum = list(a_dictionary.values())[0]
        for key, value in a_dictionary.items():
            
            if value > maximum:
                maximum = value
        for key, value in a_dictionary.items():
            if value == maximum:
                return key
    else:
        return None
