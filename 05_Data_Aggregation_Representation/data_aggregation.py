
import pandas as pd

expenses = pd.read_csv("dataset/processed/cleaned_expenses.csv")
income = pd.read_csv("dataset/processed/cleaned_income.csv")

expenses["date_time"] = pd.to_datetime(expenses["date_time"])
income["date_time"] = pd.to_datetime(income["date_time"])

expenses["year"] = expenses["date_time"].dt.year
expenses["month"] = expenses["date_time"].dt.month

income["year"] = income["date_time"].dt.year
income["month"] = income["date_time"].dt.month

expense_by_category = expenses.groupby("category")["amount"].sum().reset_index()
expense_by_category = expense_by_category.sort_values("amount", ascending=False)

expense_by_month = expenses.groupby(["year", "month"])["amount"].sum().reset_index()
expense_by_month = expense_by_month.rename(columns={"amount": "total_expense"})

income_by_month = income.groupby(["year", "month"])["amount"].sum().reset_index()
income_by_month = income_by_month.rename(columns={"amount": "total_income"})

monthly_summary = pd.merge(
    income_by_month,
    expense_by_month,
    on=["year", "month"],
    how="outer"
)

monthly_summary = monthly_summary.fillna(0)

monthly_summary["savings"] = (
    monthly_summary["total_income"] - monthly_summary["total_expense"]
)

monthly_summary = monthly_summary.sort_values(["year", "month"])

expense_by_category.to_csv(
    "outputs/reports/expense_by_category.csv",
    index=False
)

expense_by_month.to_csv(
    "outputs/reports/expense_by_month.csv",
    index=False
)

income_by_month.to_csv(
    "outputs/reports/income_by_month.csv",
    index=False
)

monthly_summary.to_csv(
    "outputs/reports/monthly_summary.csv",
    index=False
)

print("EXPENSE BY CATEGORY")
print("-------------------")
print(expense_by_category.head(10))

print()
print("MONTHLY FINANCIAL SUMMARY")
print("-------------------------")
print(monthly_summary)

print()
print("Aggregation files saved in outputs/reports/")
