#!/usr/bin/env python3
"""
# Instructions
Your classmates asked you to copy some paperwork for them.
You know that there are 'n' classmates and the paperwork has 'm' pages.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def paperwork(n, m):
    # Happy Coding! ^_^
    if n < 0 or m < 0:
        f = 0
    else:
        f = n * m
    return f


output = paperwork(5, 5)
print(output)
