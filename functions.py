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