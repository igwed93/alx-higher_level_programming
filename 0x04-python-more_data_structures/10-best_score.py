#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max = 0
        key = ""
        for k, v in a_dictionary.items():
            if v > max:
                key = k
                max = v
        return (key)
