#Task 9
items = [1, 2, 2, 3, 4, 4, 4, 5]
result = []
for i in range(1, len(items)):
    if items[i] == items[i-1] and items[i] not in result:
        result.append(items[i])
print(result)
    