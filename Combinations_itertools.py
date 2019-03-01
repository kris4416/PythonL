# Importing combinations_with_replacment function
from itertools import combinations_with_replacement

# create a list of object to combine
list_of_objects = ['warplanes', 'armor', 'infantry']

# create a empty list to hold the results of the loop
combinations = []

# create a loop for every objects in length of list_of_objects, that,
for i in list(range(len(list_of_objects))):
    combinations.append(list(combinations_with_replacement(list_of_objects, i+1)))

print(combinations)

# Flatten the row to just a list
combinations = [i for row in combinations for i in row]

print(combinations)