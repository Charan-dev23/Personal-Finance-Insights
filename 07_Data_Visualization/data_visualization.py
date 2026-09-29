import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

expense_by_category = pd.read_csv("outputs/reports/expense_by_category.csv")
monthly_summary = pd.read_csv("outputs/reports/monthly_summary.csv")

plt.figure(figsize=(10, 6))
sns.barplot(
    data=expense_by_category,
    x="amount",
    y="category"
)
plt.title("Expense by Category")
plt.xlabel("Total Expense")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("outputs/charts/expense_by_category.png")
plt.show()
plt.close()

monthly_summary["month_label"] = (
    monthly_summary["year"].astype(str)
    + "-"
    + monthly_summary["month"].astype(str).str.zfill(2)
)

plt.figure(figsize=(10, 6))
plt.plot(
    monthly_summary["month_label"],
    monthly_summary["total_income"],
    marker="o",
    label="Income"
)
plt.plot(
    monthly_summary["month_label"],
    monthly_summary["total_expense"],
    marker="o",
    label="Expense"
)
plt.title("Monthly Income vs Expense")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/charts/monthly_income_vs_expense.png")
plt.show()
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(
    monthly_summary["month_label"],
    monthly_summary["savings"]
)
plt.title("Monthly Savings")
plt.xlabel("Month")
plt.ylabel("Savings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/charts/monthly_savings.png")
plt.show()
plt.close()

print("Visualization completed successfully.")
print()
print("Charts saved in outputs/charts/")
