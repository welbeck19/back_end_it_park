#Task 13
user = {"username": "nargiza", "active": True, "role": "student"}
if user["active"] == True and user["role"] == "teacher":
    print("Yangi kurs yarata oladi")
elif user["active"] == True and user["role"] == "student":
    print("Faqat kursga yozila oladi")
else:
    print("Ruxsat yo'q")