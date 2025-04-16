import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from queries import sales_vs_cpi  # This function should take store_id and return CPI, Weekly_Sales

# Stores to compare
store_ids = [13, 21]

# Connect to DB
conn = sqlite3.connect("promotion_project.db")

# Fetch and tag data for both stores
df_list = []
for store_id in store_ids:
    query = sales_vs_cpi(store_id)
    df = pd.read_sql(query, conn)
    df["Store"] = store_id  # Add store ID to the DataFrame
    df_list.append(df)

conn.close()

# Combine dataframes
combined_df = pd.concat(df_list, ignore_index=True)

# Plot CPI vs Weekly Sales with store color-coded
plt.figure(figsize=(10, 6))
sns.scatterplot(data=combined_df, x="CPI", y="Weekly_Sales", hue="Store", palette="Set1")

plt.title(f"CPI vs Weekly Sales Comparison: Store {store_ids[0]} vs Store {store_ids[1]}")
plt.xlabel("Consumer Price Index (CPI)")
plt.ylabel("Weekly Sales")
plt.legend(title="Store")
plt.tight_layout()
plt.show()
