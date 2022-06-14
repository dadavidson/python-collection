#!/usr/bin/env python3
"""
# Instructions
Given a month as an integer from 1 to 12,
return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter;
month 6 (June), is part of the second quarter; and month 11 (November),
is part of the fourth quarter.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def quarter_of(month):
    # your code here
    q1 = [1, 2, 3]
    q2 = [4, 5, 6]
    q3 = [7, 8, 9]
    q4 = [10, 11, 12]

    if month in q1:
        return 1
    elif month in q2:
        return 2
    elif month in q3:
        return 3
    elif month in q4:
        return 4
    else:
        return None


output = quarter_of(4)
print(output)
