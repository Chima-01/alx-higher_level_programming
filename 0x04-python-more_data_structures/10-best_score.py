#!/usr/bin/python3

# This function returns a key with the biggest integer value.

def best_score(a_dictionary):
    if a_dictionary:
        highest_scorer = max(a_dictionary,
                             key=a_dictionary.get)
        return highest_scorer
    else:
        return None
