
import pandas as pd

expenses = pd.read_csv("dataset/raw/Expenses_clean.csv")
income = pd.read_csv("dataset/raw/Income_clean.csv")

print("EXPENSE DATA")
print("------------")
print("Rows and columns:", expenses.shape)
print("Columns:", list(expenses.columns))
print()
print(expenses.head())

print()
print("INCOME DATA")
print("-----------")
print("Rows and columns:", income.shape)
print("Columns:", list(income.columns))
print()
print(income.head())
