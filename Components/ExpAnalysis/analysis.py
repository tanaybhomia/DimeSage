# Part 2: Module for Analyzing Expense Data with Additional Insights

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define the Expense class
class Expense:
    def __init__(self, expense_id, user_id, amount, category, description, date):
        self.expense_id = expense_id
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.strptime(date, '%Y-%m-%d')

# Function to read data from a file and create Expense objects
def read_expense_data(file_path):
    data = pd.read_csv(file_path)
    expenses = []

    for _, row in data.iterrows():
        expense = Expense(
            row['Expense_Id'],
            row['User_Id'],
            row['Amount'],
            row['Category'],
            row['Description'],
            row['Date']
        )
        expenses.append(expense)

    return expenses

# Function to analyze spending habits and provide insights
def analyze_spending_habits(expenses):
    # Calculate total spending per month
    expenses_df = pd.DataFrame([vars(expense) for expense in expenses])
    expenses_df['Month'] = expenses_df['date'].dt.to_period('M')
    monthly_spending = expenses_df.groupby('Month')['amount'].sum()

    # Print insights
    print("\nUser Spending Insights:")
    print("========================")
    
    # Find the most expensive purchase
    most_expensive_purchase = expenses_df.loc[expenses_df['amount'].idxmax()]
    print(f"The most expensive purchase was '{most_expensive_purchase['description']}' in the amount of ${most_expensive_purchase['amount']:.2f}.")

    # Find the month with the highest spending
    highest_spending_month = monthly_spending.idxmax().strftime('%B %Y')
    print(f"The user spends the most money in the month of {highest_spending_month}.")

    # Plotting monthly spending habits
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(monthly_spending.index.astype(str), monthly_spending.values, marker='o')
    plt.title('Monthly Spending Habits')
    plt.xlabel('Month')
    plt.ylabel('Total Spending')
    plt.xticks(rotation=45)

    # Calculate category-wise spending per month
    category_wise_spending = expenses_df.groupby(['Month', 'category'])['amount'].sum().unstack()

    # Plotting category-wise spending for the latest month
    latest_month = monthly_spending.idxmax()
    plt.subplot(1, 2, 2)
    category_wise_spending.loc[latest_month].plot(kind='bar', stacked=True)
    plt.title(f'Category-wise Spending for {latest_month}')
    plt.xlabel('Category')
    plt.ylabel('Total Spending')

    plt.tight_layout()
    plt.show()

# Example usage
file_path = 'random_expenses.csv'  # Updated to use the file in the current working directory
expenses_data = read_expense_data(file_path)
analyze_spending_habits(expenses_data)