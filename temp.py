#Task 4
import moduls.mycalc
a = float(input("a = "))
b = float(input("b = "))
print(f"{a} + {b} = {moduls.mycalc.addition(a, b)}")
print(f"{a} - {b} = {moduls.mycalc.subtraction(a, b)}")
print(f"{a} * {b} = {moduls.mycalc.multiplication(a, b)}")
print(f"{a} / {b} = {moduls.mycalc.divide(a, b)}")