# List: an ordered mutable collection of objects
# Denoted by: []

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]



# Creating Lists Literally

prices = []     # The variable name is on the left of the assignment operator...
                # ...and the “literal list” is on the right. In this case, the list is empty.


# List of temperatures in degrees Fahrenheit

temps = [ 32.0, 212.0, 0.0, 81.6, 100.0, 45.3 ]

# List of famous words in computer programming

words = [ 'hello', 'world' ]

# List of car details

car_details = [ 'Toyota', 'RAV4', 2.2, 60807 ]

# Like strings, floats, and integers, lists are objects, too. Here’s an example of a list of list objects

everything = [ prices, temps, words, car_details ]

# List of literal lists

odds_and_ends = [ [ 1, 2, 3], ['a', 'b', 'c' ],
                  [ 'One', 'Two', 'Three' ] ]

print(everything)

print(odds_and_ends)

