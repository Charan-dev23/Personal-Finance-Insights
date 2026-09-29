
import pandas as pd

expenses = pd.read_csv("dataset/raw/Expenses_clean.csv")
income = pd.read_csv("dataset/raw/Income_clean.csv")

expenses["date_time"] = pd.to_datetime(expenses["date_time"], errors="coerce")
income["date_time"] = pd.to_datetime(income["date_time"], errors="coerce")

print("EXPENSE DATA VALIDATION")
print("-----------------------")
print("Missing values:")
print(expenses.isnull().sum())
print()
print("Duplicate rows:", expenses.duplicated().sum())
print("Invalid dates:", expenses["date_time"].isnull().sum())
print("Invalid amounts:", (expenses["amount"] <= 0).sum())

print()
print("INCOME DATA VALIDATION")
print("----------------------")
print("Missing values:")
print(income.isnull().sum())
print()
print("Duplicate rows:", income.duplicated().sum())
print("Invalid dates:", income["date_time"].isnull().sum())
print("Invalid amounts:", (income["amount"] <= 0).sum())

expenses = expenses.drop_duplicates()
income = income.drop_duplicates()

expenses = expenses.dropna(subset=["date_time", "category", "amount"])
income = income.dropna(subset=["date_time", "category", "amount"])

expenses = expenses[expenses["amount"] > 0]
income = income[income["amount"] > 0]

expenses.to_csv("dataset/processed/cleaned_expenses.csv", index=False)
income.to_csv("dataset/processed/cleaned_income.csv", index=False)

print()
print("CLEANED DATA")
print("------------")
print("Cleaned expenses:", expenses.shape)
print("Cleaned income:", income.shape)
print("Cleaned files saved in dataset/processed/")
