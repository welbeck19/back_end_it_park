#Task 5
words = ["python", "apple", "code", "loop"]
for i in words:
    letters = list(i)
    for letter in letters:
        new_word = letters[0] + letters[-1]
    print(new_word)