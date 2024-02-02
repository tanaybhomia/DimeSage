# models.py
class UserProfile:
    def __init__(self, user_id, income, savings, goals):
        self.user_id = user_id
        self.income = income
        self.savings = savings
        self.goals = goals

class ExpenseCategory:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

class Expense:
    def __init__(self, user_id, category_id, amount, date):
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.date = date

class FinancialScore:
    def __init__(self, user_id, score):
        self.user_id = user_id
        self.score = score