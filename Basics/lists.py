#!/usr/bin/env python3

# Lists
movies = ["The Matrix", "Harry Potter", "Saving Private Ryan", "Oxygen"]

print(movies[0])        # return the 1st item
print(movies[1])        # return the 2nd item
print(movies[1:4])      # list slicing
print(movies[1:])       # return 1-3 item
print(movies[:1])       # return 0 item stop before 1
print(movies[:-1])
print(len(movies))      # return the lenght of list

movies.append("JAWS")   # append movie to list
print(movies)

movies.pop(2)           # remove item from list
print(movies)
