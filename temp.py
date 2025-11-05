#Task 3
numbers = [7, 12, -3, 8, 0, 15]

i = 0
max = float('-inf')
min = float('inf')

while i < len(numbers):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]

    i += 1
    
print(max)
print(min)