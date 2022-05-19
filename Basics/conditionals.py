#!/usr/bin/env python3

# Conditional Statements


def drink(money):
    if (money >= 2):
        return "You've got yourself a drink!"
    else:
        return "NO drink for you!"


print(drink(3))
print(drink(1))


def alcohol(age, money):
    if (age >= 21) and (money >= 5):                # if statement
        return "we're getting a drink!"
    elif (age >= 21) and (money < 5):               # else-if statement
        return "Come back with more money!"
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:                                           # else statement
        return "You're too poor and too young"


print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 4))
