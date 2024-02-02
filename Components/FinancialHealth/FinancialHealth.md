````python
# Financial Score Calculation

## Data:

```python
# Sample data for illustration
user_profiles = {
    1: UserProfile(user_id=1, income=5000, savings=5000, goals=[{'name': 'Buy a car', 'amount': 10000, 'current_amount': 10000}, {'name': 'Vacation', 'amount': 5000, 'current_amount': 5000}]),
    # ... (other user profiles)
}

expenses = {
    1: [Expense(user_id=1, category_id=1, amount=200, date=date(2024, 1, 15)), Expense(user_id=1, category_id=2, amount=100, date=date(2024, 1, 20))],
    # ... (other expenses)
}

financial_scores = {
    1: FinancialScore(user_id=1, score=None),  # Initialize with None, to be calculated
    # ... (other financial scores)
}
```
````

## Calculation for User 1:

1. **Calculate Income vs. Expense Ratio (50% Weight):**

   - Total Income: $5000
   - Total Expenses: $200 + $100 = $300
   - Income vs. Expense Ratio: \[ \frac{5000}{300} \approx 16.67 \]

2. **Calculate Saving Rate (30% Weight):**

   - Total Income: $5000
   - Total Savings: $5000
   - Saving Rate: \[ \frac{5000}{5000} \times 100 = 100\% \]

3. **Calculate Budget Adherence (20% Weight):**

   - Total Budgeted Expenses: $200 + $100 = $300 (Assumed budgeted expenses are the same as actual expenses for simplicity)
   - Total Actual Expenses: $300
   - Budget Adherence: \[ \frac{300}{300} \times 100 = 100\% \]

4. **Calculate Goal Funding (10% Weight):**
   - Buy a Car Goal:
     - Goal Amount: $10,000
     - Current Amount Saved: $10,000
     - Goal Funding Percentage: \[ \frac{10,000}{10,000} \times 100 = 100\% \]
   - Vacation Goal:
     - Goal Amount: $5,000
     - Current Amount Saved: $5,000
     - Goal Funding Percentage: \[ \frac{5,000}{5,000} \times 100 = 100\% \]

## Apply Weights and Calculate Overall Financial Score:

\[ \text{Overall Financial Score} = 0.5 \times \text{Income vs. Expense Ratio} + 0.3 \times \text{Saving Rate} + 0.2 \times \text{Budget Adherence} + 0.1 \times \text{Goal Funding} \]

\[ \text{Overall Financial Score} = 0.5 \times 16.67 + 0.3 \times 100 + 0.2 \times 100 + 0.1 \times \left(\frac{100 + 100}{2}\right) \]

\[ \text{Overall Financial Score} \approx 8.335 + 30 + 20 + 5 = 63.335 \]

So, the final financial score for User 1 is approximately 63.335.
