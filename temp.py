#Task 3
import sqlite3
conn = sqlite3.connect("database/library.db")
cur = conn.cursor()
cur.execute("SELECT * FROM books")
books_list = cur.fetchall()

for book in books_list:
    print(book)

conn.close()