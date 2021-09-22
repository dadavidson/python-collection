#!/usr/bin/env python3

# Dictionaries - key/value pairs {}

drinks = {"Sprite": 2, "Dr. Pepper": 1, "Red Bull": 3}
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise"]}
print(employees)

employees['Legal'] = ["Mr. Frond"]                  # add new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})     # add new key:value pair
print(employees)

drinks['Red Bull'] = 8
print(drinks)

print(drinks.get('Red Bull'))
