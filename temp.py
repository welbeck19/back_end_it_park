#Task 15
user_data = {"registered": True, 
             "has_license": True,
             "age": 19
             }
if user_data["registered"] != True:
    print("Not registered")
    if user_data["has_license"] != True:
        print("Has no license") 
        if user_data["age"] != 19:
            print("Wrong age")
    print("Ijaraga ruxsat")
else:
    print("Ijaraga ruxsat")
