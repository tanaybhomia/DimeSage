# data.py
from datetime import date
from model import UserProfile, ExpenseCategory, Expense, FinancialScore  # Add this import

# Sample data for illustration
user_profiles = {
    1: UserProfile(user_id=1, income=5000, savings=1000, goals=['Buy a car', 'Vacation']),
    2: UserProfile(user_id=2, income=7000, savings=1500, goals=['Home renovation']),
}

expense_categories = {
    1: ExpenseCategory(category_id=1, name='Groceries'),
    2: ExpenseCategory(category_id=2, name='Utilities'),
}

expenses = [
    Expense(user_id=1, category_id=1, amount=200, date=date(2024, 1, 15)),
    Expense(user_id=1, category_id=2, amount=100, date=date(2024, 1, 20)),
    Expense(user_id=2, category_id=1, amount=150, date=date(2024, 1, 18)),
]

financial_scores = {
    1: FinancialScore(user_id=1, score=None),  # Initialize with None, to be calculated
    2: FinancialScore(user_id=2, score=None),
}