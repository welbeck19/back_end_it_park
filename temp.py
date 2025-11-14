#Task 4
import sqlite3
conn = sqlite3.connect("database/library.db")
cur = conn.cursor()
author_search_value = input("Type author name you are searching for: ")
cur.execute("SELECT * FROM books WHERE author = ?", (author_search_value,))

author = cur.fetchone()
print(author)