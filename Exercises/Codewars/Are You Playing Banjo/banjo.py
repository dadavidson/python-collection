#!/usr/bin/env python3
"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or "r", you are playing banjo!
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def are_you_playing_banjo(name):
    # Implement me!
    if name[0] == 'r' or name[0] == 'R':
        answer = name + " plays banjo"
    else:
        answer = name + " does not play banjo"
    return answer


output = are_you_playing_banjo(input("What is your name? "))
print(output)
