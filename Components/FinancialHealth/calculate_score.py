# calculate_score.py
from model import UserProfile, Expense, FinancialScore
from data import user_profiles, expenses, financial_scores

def calculate_income_vs_expense_ratio(user_id):
    user_profile = user_profiles[user_id]
    total_income = user_profile.income
    total_expenses = sum(expense.amount for expense in expenses if expense.user_id == user_id)
    
    ratio = total_income / total_expenses if total_expenses != 0 else 0
    return ratio

def calculate_saving_rate(user_id):
    user_profile = user_profiles[user_id]
    total_income = user_profile.income
    total_savings = user_profile.savings
    
    saving_rate = (total_savings / total_income) * 100
    return saving_rate

def calculate_budget_adherence(user_id):
    user_profile = user_profiles[user_id]
    total_budgeted_expenses = sum(expense.amount for expense in expenses if expense.user_id == user_id)
    total_actual_expenses = sum(expense.amount for expense in expenses if expense.user_id == user_id)
    
    adherence = (total_actual_expenses / total_budgeted_expenses) * 100 if total_budgeted_expenses != 0 else 0
    return adherence

def calculate_goal_funding(user_id):
    user_profile = user_profiles[user_id]
    total_goals = len(user_profile.goals)
    achieved_goals = 0  # For simplicity, assuming all goals are achieved in this example
    
    goal_funding = (achieved_goals / total_goals) * 100 if total_goals != 0 else 0
    return goal_funding

def calculate_financial_score(user_id):
    income_vs_expense_ratio = calculate_income_vs_expense_ratio(user_id)
    saving_rate = calculate_saving_rate(user_id)
    budget_adherence = calculate_budget_adherence(user_id)
    goal_funding = calculate_goal_funding(user_id)

    # Apply the specified weights to each criterion
    score = (
        0.5 * income_vs_expense_ratio +
        0.3 * saving_rate +
        0.2 * budget_adherence +
        0.1 * goal_funding
    )

    # Update the financial score in the in-memory database
    financial_scores[user_id].score = score

    return score

if __name__ == "__main__":
    # Calculate and print financial scores for all users
    for user_id in user_profiles:
        score = calculate_financial_score(user_id)
        print(f"Financial Score for User {user_id}: {score}")