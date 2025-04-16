import numpy as np
import pandas as pd
import sqlite3

# Load the CSV
df = pd.read_csv("sales.csv")  # Update path if needed

# Check the data
print(df.head())

# Connect to a SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("promotion_project.db")

# Save the DataFrame as a table named 'sales'
df.to_sql("sales", conn, if_exists="replace", index=False)

# Confirm it worked (optional)
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in DB:", tables)

# Close the connection
conn.close()
