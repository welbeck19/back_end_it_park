#Task 1
user_age = input("Type your age: ")
if user_age < 18:
    print("Underaged")
else:
    print("Adult")

#Task 2
score = 87
if score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
else:
    print("D")

#Task 3
is_raining = False
if is_raining:
    print("Soyabon oling")
else:
    print("Yomg'ir yo'q")


#Task 4
fruits = ["olma", "banan", "gilos"]
if "banan" in fruits:
    print("Banan bor")
else:
    print("Banan yo'q")

#Task 5
nums = [1, 4, 7, 10]
if len(nums) >= 5:
    print("Ro'yhat to'la")
else:
    print("Ro'yhat qisqa")

#Task 6
location = (41.2, 69.1)
if len(location) == 2:
    print("Joylashuv aniqlangan")
else:
    print("Joylashuv yo'q")

#Task 7
active_ids = {1, 2, 3}
if 2 in active_ids:
    print("2-ID mavjud")
else:
    print("2-ID yo'q")

#Task 8
profile = {"name": "Alim", "age": 15}
if profile["age"] >= 18:
    print("Voyaga yetgan")
else:
    print("Voyaga yetmagan")

#Task 9
is_logged_in = True
is_admin = False
if is_logged_in and is_admin:
    print("Admin panelga xush kelibsiz")
elif is_logged_in:
    print("Foydalanuvchi paneli")
else:
    print("Kirish talab qilinadi")