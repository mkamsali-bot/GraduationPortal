import sqlite3

conn = sqlite3.connect("students.db")
conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("SELECT * FROM students")

students = cur.fetchall()

for student in students:
    print(dict(student))

conn.close()