#!/usr/bin/env python3
"""
# Instructions
Given a string, you have to return a string in which
each character (case-sensitive) is repeated once.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def double_char(s):
    char_list = []
    for c in s:
        char_list.append(c * 2)
    return ''.join(char_list)


ouput = double_char("String")
print(ouput)
