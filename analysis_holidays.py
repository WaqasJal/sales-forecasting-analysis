import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from queries import store_sales_with_holidays
store_id = 40

# Connect to DB and get data for one store (e.g., Store 1)
conn = sqlite3.connect("promotion_project.db")
query = store_sales_with_holidays(store_id)  # You can change store ID
df = pd.read_sql(query, conn)
conn.close()

# Convert date to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")


# Separate holiday and non-holiday data
holiday_df = df[df["Holiday_Flag"] == 1]
non_holiday_df = df[df["Holiday_Flag"] == 0]

# Plot
sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))
plt.plot(non_holiday_df["Date"], non_holiday_df["Weekly_Sales"],'o', label="Non-Holiday", color="skyblue")
plt.plot(holiday_df["Date"], holiday_df["Weekly_Sales"], 'o', label="Holiday", color="red")

plt.title(f"Store {store_id} Weekly Sales (Holidays Highlighted)")
plt.xlabel("Date")
plt.ylabel("Weekly Sales")
plt.legend()
plt.tight_layout()
plt.show()
