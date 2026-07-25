import sqlite3

conn = sqlite3.connect("students.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (

    regno TEXT PRIMARY KEY,

    name TEXT,

    degree TEXT,

    institute TEXT,

    program TEXT,

    branch TEXT,

    ceremony_date TEXT,

    grad_row TEXT,
    grad_seat TEXT,

    cert_row TEXT,
    cert_seat TEXT,

    parent_venue TEXT,

    photo TEXT

)
""")

conn.commit()

conn.close()

print("Database Created Successfully")