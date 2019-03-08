from array import *

array1 = array('i', [10, 20, 30, 40, 50])

array1.insert(len(array1)+1, 60)

for x in array1:
    print(x)

array1.remove(array1[len(array1)-1])

for x in array1:
    print(x)

print(array1.index(30))