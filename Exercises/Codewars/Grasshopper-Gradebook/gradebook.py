#!/usr/bin/env python3
"""
# Instructions
Complete the function so that it finds the average of the three scores passed
to it and returns the letter value associated with that grade.

Tested values are all between 0 and 100. Theres is no need to check for
negative values or values greater than 100.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"


output = get_grade(80, 70, 65)
print(output)
