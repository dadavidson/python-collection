#!/usr/bin/env python3
"""
# Instructions
Convert number to reversed array of digits

Given a random non-negative number, you have
to return the digits of this number within an
array in reverse order.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def digitize(n):
    i = str(n)                      # Convert input integer -> string
    list_store = []                 # Initialize empty list
    for e in i[len(i)::-1]:         # Get input length & str slice in reverse
        list_store.append(int(e))   # Append each character to list
    return list_store


output = digitize(348597)           # Input random number
print(output)                       # Output
