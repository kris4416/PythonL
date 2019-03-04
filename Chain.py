# Importing Chain from itertools
from itertools import chain

# Create a list of allies
allies = ['Spain', 'Germany', 'Namibia', 'Austria']

# Create a list of enemies
enemies = ['Mexico', 'United Kingdom', 'France']

for country in chain(allies, enemies):
    print(country)
