import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Clear existing records (optional during development)
cur.execute("DELETE FROM students")

# Insert a sample student
cur.execute("""
INSERT INTO students (
    regno,
    name,
    degree,
    institute,
    program,
    branch,
    ceremony_date,
    grad_row,
    grad_seat,
    cert_row,
    cert_seat,
    parent_venue,
    photo
)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
""",
(
    "HU22CSEN0100479",
    "PRIYANSHU DASH",
    "UG",
    "GSCSE",
    "BTECH",
    "CSE",
    "01-08-2026",
    "A",
    "15",
    "",
    "",
    "Helipad Arena",
    "HU22CSEN0100479.jpg"
))

conn.commit()
conn.close()

print("Student Added Successfully")