#!/usr/bin/env python3
"""
# Instructions
Create a function which translates a given DNA string into RNA.
"""

__author__ = "Daniel Davidson"
__version__ = "0.1.0"
__license__ = "MIT"


def dna_to_rna(dna):
    data = dna.replace('T', 'U')
    return data


output = dna_to_rna('GCAT')
print(output)
