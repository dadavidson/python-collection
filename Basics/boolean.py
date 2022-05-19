#!/usr/bin/env python3

# Boolean Expressions

print("Boolean expressions:")

bool1 = True            # True
bool2 = 3*3 == 9        # True
bool3 = False           # False
bool4 = 3*3 != 9        # False

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"          # Not a boolean value
print(type(bool5))      # This is a string
