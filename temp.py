#Task 6
nums = [5, 9, 15, 20, 22, 30, 35]
result = []

for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        result.append(num)

average = sum(result) / len(result)
print(average)