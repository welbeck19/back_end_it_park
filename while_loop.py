#Task 1
number = int(input("Type a number: "))
result = 0
i = 0
while i <= number:
    result += i
    i += 1
print(result)

#Task 2
words = ["apple", "sky", "queue", "book", "cry"]
vowels = "aeiouAEIOU"
count = 0
i = 0
while i < len(words):
    vowel_count = 0
    for letter in words[i]:
        if letter in vowels:
            vowel_count += 1
    if vowel_count >= 2:
        count += 1
    i += 1
print(count)

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