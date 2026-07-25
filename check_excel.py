import pandas as pd

# Read the Excel file
df = pd.read_excel("data/students.xlsx")

# Display the column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display the first five records
print("\nFirst 5 Records:")
print(df.head())