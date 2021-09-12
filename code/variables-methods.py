#!/usr/bin/env python3

# Variables and Methods
quote = "All is fair in love and war."
print(quote)

print(quote.upper())        # UPPERCASE
print(quote.lower())        # lowercase
print(quote.title())        # Titlecase

print(len(quote))           # Get char length of string

name = "Daniel"             # string str(name)
age = 30                    # int int(30)
gpa = 3.0                   # float float(3.0)

print(int(age))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1                    # age = age + 1
print(age)

birthday = 1
age += birthday             # age = age + birthday
print(age)
