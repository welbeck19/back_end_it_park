# class yaratish
# Book classini yarating. U quyidagi atributlarga ega bo'lishi kerak:
# title(nomi)
# author(muallifi)
# year(nashr yili)
# Shuningdek, classda display_info metodini qo'shing, u kitob haqida 
# ma'lumotlarni chiqarishi kerak.
# class Book:
#     # Bu yerga kod yozing

#17-OOP
# Task 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"Book name: {self.title}, Author: {self.author}, Year: {self.year}"

book1 = Book("Hi", "John", 2020)

print(book1.display_info())


