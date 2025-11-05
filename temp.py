#Task 11
skills = ["html", "python", "css"]
if "python" and "sql" in skills:
    print("Ikkalasi ham bor")
elif ("python" in skills) ^ ("sql" in skills):
    print("Bittasi bor")
else:
    print("Ikkalasi ham yo'q")