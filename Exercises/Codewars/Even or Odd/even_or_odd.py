#!/usr/bin/env python3
"""
# Instructions
Create a function that takes an integer as an argument and
returns "Even" for even numbers or "Odd" for odd numbers.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def even_or_odd(number):
    number = number % 2
    if number == 0:
        return "Even"
    else:
        return "Odd"


output = even_or_odd(3)
print(output)
