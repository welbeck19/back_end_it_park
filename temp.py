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

