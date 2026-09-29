
import pandas as pd

expenses = pd.read_csv("dataset/raw/Expenses_clean.csv")
income = pd.read_csv("dataset/raw/Income_clean.csv")

expense_columns = ["date_time", "category", "account", "amount", "currency", "tags"]
income_columns = ["date_time", "category", "account", "amount", "currency", "tags"]

expenses = expenses[expense_columns]
income = income[income_columns]

expenses = expenses[expenses["amount"] > 0]
income = income[income["amount"] > 0]

print("FILTERED EXPENSE DATA")
print("---------------------")
print("Rows and columns:", expenses.shape)
print()
print(expenses.head())

print()
print("FILTERED INCOME DATA")
print("--------------------")
print("Rows and columns:", income.shape)
print()
print(income.head())
