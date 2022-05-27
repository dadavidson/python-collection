#!/usr/bin/env python3
"""
# Instructions
Complete the solution so that it splits the string into pairs of 2 characters.
If the string contains an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def split_strings(test_subject):
    # return your answer
    n = 2
    list_store = []
    if len(test_subject) % 2 != 0:
        test_subject = test_subject + "_"

    for i in range(0, len(test_subject), n):
        list_store.append(test_subject[i:i + 2])

    return list_store


output = split_strings("abcd")
print(output)
