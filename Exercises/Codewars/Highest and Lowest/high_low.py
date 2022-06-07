#!/usr/bin/env python3
"""
# Instructions
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def high_and_low(numbers):
    # your code here
    numbers = numbers.split()
    numbers = [int(item) for item in numbers]
    numbers = sorted(numbers)
    low = str(numbers[0])
    high = str(numbers[-1])
    numbers = high + ' ' + low
    return numbers


output = high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print(output)
