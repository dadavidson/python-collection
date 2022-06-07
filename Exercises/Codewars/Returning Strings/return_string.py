#!/usr/bin/env python3
"""
# Instructions
Make a function that will return a greeting statement that uses an input;
your program should return, "Hello, <name> how are you doing today?".
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def greet(name):
    return f'Hello, {name} how are you doing today?'


output = greet('Roger')
print(output)
