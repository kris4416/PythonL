regimentSize = (5345, 6436, 3453, 2352, 5212, 6232, 2124, 3425, 1200, 1000, 1211)

print(regimentSize)

smallRegiment = list(filter(lambda x: x < 2500, regimentSize))

print(smallRegiment)

smallRegiment1 = []

for i in regimentSize:
    if i < 2500:
        smallRegiment1.append(i)

print(smallRegiment1)

commander_names = ["Alan Brooke", "George Marshall", "Frank Jack Fletcher", "Conrad Helfrich", "Albert Kesselring"]

names = list(filter(lambda x: x.split(" "), commander_names))

print(names)
