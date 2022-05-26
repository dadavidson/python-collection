#!/usr/bin/env python3
"""
# Instructions
You are given the `length` and `width` of a 4-sided polygon.
The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def area_or_perimeter(ln, wn):
    # return your answer
    if ln == wn:
        # Area
        print("The area is: ", end="")
        answer = ln * wn
    else:
        # Perimeter
        print("The perimeter is: ", end="")
        answer = (ln + wn) * 2
    return answer


output = area_or_perimeter(320, 320)
print(output)
