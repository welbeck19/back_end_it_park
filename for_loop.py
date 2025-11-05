#for_loop
#Task 1
number = int(input("Type integer: "))
result = 0
for i in range(number):
    result += i + 1
print(result)

#Task 2
words = ["apple", "sky", "queue", "book", "cry"]
for i in words:
    count = 0
    word = list(i)
    for letter in word:
        vowels = ["a", "e", "o", "u", "i"]
        if letter in vowels:
            count += 1
        else:
            continue
    if count >= 2:
        print(f"Number of vowels in {i}: {count}")

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

#Task 4
numbers = [0, 1, 2, 3, -4, 8, -100, 23, 55, 66]
positive_odd = []
for i in numbers:
    if i > 0 and i % 2 != 0:
        positive_odd.append(i)
print(positive_odd)

#Task 5
words = ["python", "apple", "code", "loop"]
for i in words:
    letters = list(i)
    for letter in letters:
        new_word = letters[0] + letters[-1]
    print(new_word)
