# Define a list of vowels

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"

for letter in word:             # Take each letter in the word...
    if letter in vowels:        # and if it is in the “vowels” list...
        print(letter)           # display the letter on screen.


#Growing a list at runtime

found = []                      # An empty list...    
len(found)                      # which the interpreter (thanks to “len”) confirms has no objects.

# Use the append method to add an object to the end of the empty list we just created:

found.append('a')                 # Add to an existing list at runtime using the “append” method.
len(found)                      # The length of the list has now increased.


found.append('e')
found.append('i')
found.append('o')
found.append('u')

len(found)

print(found)
