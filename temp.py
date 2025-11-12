#Task 3
try:
    operators = ["+", "-", "*", "/"]
    a = input("Type first number: ")
    b = input("Type second number: ")
    operator = input("Type an operator: ")
    if operator not in operators: 
        print("Wrong operator!")
except Exception as e:
    print(e)