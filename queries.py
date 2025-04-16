import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("promotion_project.db")

def get_all_sales(conn):
    query = "SELECT * FROM sales"
    return pd.read_sql(query, conn)

def get_sales_by_store(store_id):
    query = f"""
        SELECT Date, Weekly_Sales
        FROM sales
        WHERE Store = {store_id}
        ORDER BY Date
    """
    return pd.read_sql(query, conn)


def get_avg_sales_per_store(conn):
    query = """
    SELECT Store, ROUND(AVG(Weekly_Sales), 2) AS avg_sales
    FROM sales
    GROUP BY Store
    ORDER BY avg_sales DESC
    """
    return pd.read_sql(query, conn)

def store_sales_with_holidays(store_id):
    return f"""
    SELECT 
        Date, 
        Weekly_Sales, 
        Holiday_Flag
    FROM sales
    WHERE Store = {store_id}
    ORDER BY Date ASC
    """
# def sales_vs_cpi(store_id):
#     return f"""
#     SELECT 
#         Date,
#         Weekly_Sales,
#         CPI,
#         Holiday_Flag
#     FROM sales
#     WHERE Store = {store_id}
#     ORDER BY Date ASC
#     """

def sales_vs_cpi(store_id):
    return f"""
    SELECT 
        CPI,
        Weekly_Sales
    FROM sales
    WHERE Store = {store_id}
    ORDER BY Date ASC
    """





# Optional: close connection at the end (or move to main file)
# conn.close()
