#File handling 
#Task 1
f = open("example.txt", "r")
content = f.read()
print(content)

#Task 2
name = input("Type your name: ")
surname = input("Type your surname: ")
age = input("Type your age: ")
user_info = f"User name: {name}, surname: {surname}, age: {age} \n"
f = open("info.txt", "a")
f.writelines(user_info)
f.close()
f = open("info.txt", "r")
content = f.read()
print(content)

#Task 3
f = open('file_handling/numbers.txt', 'w')
numbers = ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n']
f.writelines(numbers)
f.close()
f = open('file_handling/numbers.txt', 'r')
content = f.read()
print(content)
f.close()

#Task 4
import re
f = open('file_handling/numbers.txt', 'r')
content = f.read()
numbers = re.findall(r"\d+", content)
for i in numbers:
    result = int(i) * 2
    print(result)
f.close()

#Task 5
f = open('file_handling/append_example.txt', 'a')
f.write('New line\n')
f.close()

#Task 6
text1 = input("Type your first sentence: ")
text2 = input("Type your second sentence: ")
text3 = input("Type your third sentence: ")
text_joined = f"{text1}\n{text2}\n{text3}"
f = open("file_handling/sentences.txt", "w")
f.writelines(text_joined)
