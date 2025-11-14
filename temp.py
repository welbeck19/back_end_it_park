#Task 5
import sqlite3
conn = sqlite3.connect("database/library.db")
cur = conn.cursor()

cur.execute("UPDATE books SET year = ? WHERE title = ?", (2019, "SQL for Beginners"))
conn.commit()

cur.execute("SELECT * FROM books WHERE title = ?", ("SQL for Beginners",))
book = cur.fetchone()
print(book)

conn.close()
