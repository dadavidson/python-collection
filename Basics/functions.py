#!/usr/bin/env python3

# Functions


def who_am_i():             # this is a function declaration
    name = 'Daniel'
    age = 30
    print("My name is " + name + " and I am " + str(age) + " years old.")


who_am_i()                  # calling a function


def add_one_hundred(num):   # adding parameters
    print(num + 100)


add_one_hundred(100)


def add(x, y):              # multiple parameters
    print(x + y)


add(7, 7)


def multiply(x, y):         # multiply
    return x * y


print(multiply(7, 7))


def square_root(x):         # square root
    print(x ** .5)


square_root(64)


def nl():                   # newline
    print('\n')


nl()
