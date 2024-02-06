# Part 1: Generate Random Expense Data

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate random expense data
np.random.seed(42)

num_entries = 100
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

user_ids = np.random.choice(range(1, 6), num_entries)
amounts = np.random.uniform(10, 100, num_entries)
categories = np.random.choice(['Groceries', 'Entertainment', 'Utilities', 'Dining', 'Shopping'], num_entries)
descriptions = [f'Description_{i}' for i in range(1, num_entries + 1)]
dates = [start_date + timedelta(days=np.random.randint((end_date - start_date).days)) for _ in range(num_entries)]

data = {
    'Expense_Id': range(1, num_entries + 1),
    'User_Id': user_ids,
    'Amount': amounts,
    'Category': categories,
    'Description': descriptions,
    'Date': [date.strftime('%Y-%m-%d') for date in dates],
}

# Save random data to a CSV file in the current working directory
random_data_path = 'random_expenses.csv'
random_data_df = pd.DataFrame(data)
random_data_df.to_csv(random_data_path, index=False)

# Print the generated random data path
print(f"Generated random expense data saved to: {random_data_path}")
