#!/usr/bin/env python3
"""
# Instructions
Create a Python class that takes a name.
example usage: Python('Bubba')
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


class Python(object):
    def __init__(self, name):
        self.name = name


output = Python('Bubba')
print(output.name)
