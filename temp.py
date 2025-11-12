#Task 4
def check_number(number):
    if number < 0:
        raise ValueError("Manfiy son kiritish mumkin emas!")
    return number

try:
    print(f"Result: {check_number(3)}")
except ValueError as e:
    print(e)