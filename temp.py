#Task 10
text = input("Type your text: ").strip()
letters = list(text)
print(letters)
result = []
for letter in letters:
    if letter == " ":
        continue
    elif letter == letter.title():
        result.append(letter)
    else:
        continue
joined_result = "".join(result)
print(joined_result)