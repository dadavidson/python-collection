#!/usr/bin/env python3
"""
# Instructions
In this simple assignment you are given a number and have to make it negative.
But maybe the number is already negative?
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def make_negative(number):
    if number < 0:
        return number
    elif number > 0:
        return -number
    else:
        return 0


output = make_negative(2)
print(output)
