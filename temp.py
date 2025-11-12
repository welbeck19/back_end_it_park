#Task 6
def input_password(password):
    
    if not password:
        raise ValueError("Empty password!")
    
password = input("Type your password: ")

try:
    input_password(password)
except Exception as e:
    print(e)