#Task 12
while True:
    user_password = input("Please type your password: ")
    if len(user_password) > 10:
        print("Strong password!")
    elif 6 <= len(user_password) <= 10:
        print("Average password!")
    elif len(user_password) < 6:
        print("Too short password!")