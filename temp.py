#Task 4
numbers = [0, 1, 2, 3, -4, 8, -100, 23, 55, 66]
positive_odd = []
for i in numbers:
    if i > 0 and i % 2 != 0:
        positive_odd.append(i)
print(positive_odd)