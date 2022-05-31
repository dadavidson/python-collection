#!/usr/bin/env python3
"""
# Instructions
Complete the square sum function so that it squares
each number passed into it and then sums the results together.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def square_sum(*numbers):
    # your code here
    results = []
    for n in numbers:
        results.append(n ** 2)

    return sum(results)


output = square_sum(0, 3, 4, 5)
print(output)
