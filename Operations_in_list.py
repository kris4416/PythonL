# create a list of casualties in a battle
battleDeaths = [482, 93, 392, 920, 813, 199, 374, 237, 244]


# create a function that updates all battle Deaths by adding 100
def updated(x):
    return x + 100


print(list(map(updated, battleDeaths)))


# Method 2

print(list(map(lambda x: x+100, battleDeaths)))