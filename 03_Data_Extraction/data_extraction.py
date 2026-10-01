
import pandas as pd

expenses = pd.read_csv("dataset/raw/Expenses_clean.csv")
income = pd.read_csv("dataset/raw/Income_clean.csv")

expenses = expenses[expenses["amount"] > 0]
income = income[income["amount"] > 0]

expenses["date_time"] = pd.to_datetime(expenses["date_time"])
income["date_time"] = pd.to_datetime(income["date_time"])

expenses["year"] = expenses["date_time"].dt.year
expenses["month"] = expenses["date_time"].dt.month
expenses["month_name"] = expenses["date_time"].dt.month_name()

income["year"] = income["date_time"].dt.year
income["month"] = income["date_time"].dt.month
income["month_name"] = income["date_time"].dt.month_name()

print("EXTRACTED EXPENSE DATA")
print("----------------------")
print(expenses[["date_time", "category", "amount", "year", "month", "month_name"]].head())

print()
print("EXTRACTED INCOME DATA")
print("---------------------")
print(income[["date_time", "category", "amount", "year", "month", "month_name"]].head())

output 
EXTRACTED EXPENSE DATA
----------------------
   date_time          category  amount  year  month month_name
0 2025-11-30            Health   114.0  2025     11   November
1 2025-11-29              Food     5.0  2025     11   November
2 2025-11-27  Public transport     1.0  2025     11   November
3 2025-11-27              Cafe    10.0  2025     11   November
4 2025-11-27  Public transport     1.0  2025     11   November

EXTRACTED INCOME DATA
---------------------
   date_time     category  amount  year  month month_name
0 2025-11-29          Job    49.0  2025     11   November
1 2025-11-29          Job    18.0  2025     11   November
2 2025-11-29          Job    32.0  2025     11   November
3 2025-11-29          Job   109.0  2025     11   November
4 2025-11-28  Second work   132.0  2025     11   November
