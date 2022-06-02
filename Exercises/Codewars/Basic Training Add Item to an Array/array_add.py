#!/usr/bin/env python3
"""
# Instructions
Add the value "codewars" to the websites array.
After your code executes the websites array should == ["codewars"]
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def array_add(input_value):
    # your code here
    websites = []
    websites.append(input_value)
    return websites


output = array_add('codewars')
print(output)
