# Create a function that
def function(names):
    x = []
    # For each name in a list of names
    for name in names:
        x.append(name)
    # Returns the name
    return x


# Create a variable of that function
nms = ['Abe', 'Bob', 'Christina', 'Derek', 'Eleanor']
students = function(nms)

# Run the function
print(students)

names = ['James', 'Bob', 'Sarah', 'Marco', 'Nancy', 'Sally', 'A']
ages = [42, 13, 14, 25, 63, 23]

for name, age in zip(names, ages):
    print(name, age)

# Create two lists
squads = ["1st Squad", '2nd Squad', '3rd Squad']
regiments = ["51st Regiment", '15th Regiment', '12th Regiment']

print([(j, i) for j in regiments for i in squads])
