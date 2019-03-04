# Importing Random
import random

rolling=True

while rolling:
    x = random.randint(0, 99)
    y = random.randint(0, 99)

    if x < 2 and 0 < y < 10 :
        print('You rolled a {0}{1}'.format(x,y))
        rolling = False
    else:
        print('Try Again')