#Task 3
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


