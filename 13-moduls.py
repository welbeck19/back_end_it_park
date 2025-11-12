#Task 1
from math import sqrt
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(numbers)):
    sq_root = sqrt(numbers[i])
    print(round(sq_root, 2))

#Task 2
import random
numbers = [random.randint(0, 100) for i in range(5)]
print(numbers)

#Task 3
import datetime
print(datetime.datetime.now())

