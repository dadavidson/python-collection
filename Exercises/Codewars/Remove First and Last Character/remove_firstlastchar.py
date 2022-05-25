#!/usr/bin/env python3
"""
# Instructions
It's pretty straightforward. Your goal is to create a function that removes the
first and last characters of a string. You're given one parameter, the original
string. You don't have to worry with strings with less than two characters.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def remove_char(s):
    # your code here
    o = s[1:(len(s) - 1)]
    return o


output = remove_char('test')
print(output)
