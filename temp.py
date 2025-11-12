#Exception handling
#Task 2
try:
    a = float(input("Type any integer: "))
    print(a)
except Exception as e:
    print("You typed a string!!!")