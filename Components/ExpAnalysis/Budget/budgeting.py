# Import necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'random_expenses.csv'
expenses_df = pd.read_csv(file_path)

# Function to calculate and display budget for all categories
def show_budget_for_all_categories(user_id, month):
    # Filter expenses for the specified user and month
    user_expenses = expenses_df[(expenses_df['User_Id'] == user_id) & 
                                (expenses_df['Date'].str.startswith(month))]

    # Group by category and calculate total spending
    category_expenses = user_expenses.groupby('Category')['Amount'].sum().reset_index()

    # AI-generated budget formula (adjusted for lower budget)
    category_expenses['AI_Budget'] = category_expenses['Amount'] * 0.8  # Adjust as needed

    # Display results
    print(f"💳 Monthly Budget Overview - {month} 💳")
    print("📈 Budget for All Categories:")
    
    for index, row in category_expenses.iterrows():
        category = row['Category']
        total_spending = row['Amount']
        ai_generated_budget = row['AI_Budget']
        
        print(f"\n📊 Category: {category}")
        print(f"Total Spending: ${total_spending:.2f}")
        print(f"AI-Generated Budget: ${ai_generated_budget:.2f}")

        # Provide more specific tips based on category
        if category == 'Utilities':
            print("Tips:")
            print("1. Upgrade to energy-efficient appliances to reduce electricity consumption.")
            print("2. Unplug chargers and electronic devices when not in use.")
        elif category == 'Dining':
            print("Tips:")
            print("1. Plan meals ahead to avoid last-minute dining expenses.")
            print("2. Consider cooking at home to save on dining costs.")
        elif category == 'Groceries':
            print("Tips:")
            print("1. Create a shopping list and stick to it to avoid unnecessary purchases.")
            print("2. Take advantage of sales and discounts when grocery shopping.")
        elif category == 'Entertainment':
            print("Tips:")
            print("1. Explore free or low-cost entertainment options in your area.")
            print("2. Look for discounts or loyalty programs for entertainment activities.")
        elif category == 'Shopping':
            print("Tips:")
            print("1. Prioritize needs over wants when shopping.")
            print("2. Wait for sales or promotions before making non-essential purchases.")

# Example usage
show_budget_for_all_categories(user_id=4, month='2023-09')
