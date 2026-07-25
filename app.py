from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# ----------------------------------------------------
# Project Folder
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(BASE_DIR, "students.xlsx")
print("BASE_DIR :", BASE_DIR)
print("EXCEL_FILE :", EXCEL_FILE)
print("FILE EXISTS :", os.path.exists(EXCEL_FILE))


# ----------------------------------------------------
# Load Student Database
# ----------------------------------------------------
def load_students():

    if not os.path.exists(EXCEL_FILE):
        raise FileNotFoundError(
            f"\n\nstudents.xlsx NOT FOUND\n\nExpected Location:\n{EXCEL_FILE}\n"
        )

    df = pd.read_excel(EXCEL_FILE)

    # Remove unwanted spaces in column names
    df.columns = df.columns.str.strip()

    # Convert RegNo to string for searching
    df["RegNo"] = df["RegNo"].astype(str).str.strip()

    return df


# ----------------------------------------------------
# Home Page
# ----------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------------------------------
# Search Admit Card
# ----------------------------------------------------
@app.route("/search", methods=["POST"])
def search():

    reg_no = request.form.get("regno", "").strip()

    students = load_students()

    student = students[
        students["RegNo"].str.upper() == reg_no.upper()
    ]

    if student.empty:
        return render_template(
            "error.html",
            message="Registration Number not found."
        )

    student = student.iloc[0]

    return render_template(
        "admitcard.html",
        student=student
    )


# ----------------------------------------------------
# Main
# ----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)