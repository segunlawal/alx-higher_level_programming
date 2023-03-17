#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        _max = 0
        for i, j in a_dictionary.items():
            if j > _max:
                _max = j
                item = i
        return a_dictionary[item]
    return None
