#FUNCTIONS
#Task 1
def hello():
    print("ssalomu aleykum!")

hello()


#Task 2
def to_square(x):
    return x ** 2
a = float(input("Type any integer: "))
print(to_square(a))

#Task 3
def multiply(a, b):
    return a * b
x = float(input("Type a = "))
y = float(input("Type b = "))
print(multiply(x, y))

#Task 4
def say_hello(name):
    print(f"Salom, {name}")

say_hello(input())

#Task 5
def power(base, exponent=2):
    return base ** exponent
base = float(input("Type base: "))
exponent = float(input("Type your exponent: "))
print(power(base, exponent))

#Task 6
def show_list(items):
    for word in items: 
        print(word)

list_1 = ["I", "am", "your", "father"]
show_list(list_1)

#Task 7
def print_line():
    for i in range(0, 41):
        print("-")

print_line()

#Task 8

def get_max(a, b):
    return max(a, b)

print(get_max(3, 7))

#Task 9
def sum_all(*numbers):
    return sum(*numbers)

tuple_1 = (1, 2, 3, 4, 5)
print(sum_all(tuple_1))

#Task 10
def user_info(**users):
    for key, value in users.items():
        print(f"{key}: {value}")

userlar = {"name": "Ali", "age": 25}

user_info(**userlar)

#Task 11
ages = [19, 21, 17, 25]

sorted_ages = lambda x: sorted(x)
print(sorted_ages(ages))

#Task 12
def outer(x, y):
    def inner(a, b):
        return a + b
    return inner(x, y)
print(outer(6, 7))

#Task 13
def factorial(n):
    if n < 0:
        return "Negative number"
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

num = int(input("Type a positive integer: "))
result = factorial(num)
print(f"{num}! = {result}")


#Task 14
def add_numbers(a: int, b: int) -> int:
    return a + b

num1 = int(input("first number: "))
num2 = int(input("second number: "))

print(add_numbers(num1, num2))

#Task 15
def subtract(a, b):
    """
    Ikki sonni ayiradi va natijani qaytaradi.
    """
    return a - b

doc_string = subtract.__doc__
print(doc_string)
result = subtract(10, 3)
print(f"Result: {result}")
