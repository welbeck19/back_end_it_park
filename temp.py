#Task 3
numbers = [7, 12, -3, 8, 0, 15]
max = float('-inf')
min = float('inf')
for i in numbers:
    if i > max:
        max = i
print(f"Max value = {max}")
for i in numbers:
    if i < min:
        min = i
print(f"Min value = {min}")
print(f"Max - Min = {max - min}")