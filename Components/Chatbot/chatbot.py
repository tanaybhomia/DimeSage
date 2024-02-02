import re
import csv
from datetime import datetime, timedelta
from dateutil.parser import parse
from fuzzywuzzy import fuzz

def find_item(query, items, threshold=80):
    max_ratio = 0
    best_match = None

    query = query.lower().strip()

    for item in items:
        # Use partial_ratio for better matching, especially with multi-word items
        ratio = fuzz.partial_ratio(query, item.lower())
        if ratio > max_ratio and ratio >= threshold:
            max_ratio = ratio
            best_match = item

    return best_match

def parse_relative_date(date):
    if date.lower() == "yesterday":
        return datetime.now() - timedelta(days=1)
    elif date.lower() == "today":
        return datetime.now()
    elif date.lower() == "tomorrow":
        return datetime.now() + timedelta(days=1)
    else:
        return None

def parse_price(price_str):
    # Remove commas and convert to integer
    return int(price_str.replace(',', ''))

def add_new_item_to_csv(item, category):
    # Append the new item to the CSV file on a new line
    with open('dataset.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([item.lower(), category.lower()])

def chatbot():
    while True:
        query = input("Enter the query: ")

        # Using regular expression to extract item and price from the sentence
        match = re.search(r'I\s+bought\s+a\s+(.+?)\s+for\s+([\d,]+)\s*rs', query, re.IGNORECASE)
        
        if match:
            item, extracted_price = match.groups()
            price = parse_price(extracted_price) if extracted_price else None
        else:
            # Handle invalid input
            print("Invalid input format. Please use the format: 'I bought a [Item] for [Price]'.")
            continue

        if not price:
            # Prompt user to enter price if not provided
            print("Price not provided. Please enter the price in a separate query.")
            continue

        # Prompt user to enter the date of purchase
        date = input("Enter the date of purchase (e.g., DD-MM-YYYY, yesterday, today, tomorrow): ")

        # Validate and format the entered date
        parsed_relative_date = parse_relative_date(date)

        if parsed_relative_date:
            formatted_date = parsed_relative_date.strftime("%d-%m-%Y")
        else:
            try:
                parsed_date = parse(date, fuzzy_with_tokens=True)
                formatted_date = parsed_date[0].date().strftime("%d-%m-%Y")
            except ValueError:
                print("Invalid date format. Please use the format: DD-MM-YYYY or common phrases like yesterday, today, tomorrow.")
                continue

        # Load items from the dataset.csv file
        with open('dataset.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            items = [row[0].lower() for row in reader]

        # Fuzzy matching to find the correct item
        matched_item = find_item(item.lower(), items)

        if matched_item:
            # Check if the matched item is present in the dataset.csv file
            with open('dataset.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if matched_item.lower() == row[0].lower():
                        category = row[1]
                        break
                else:
                    category = "Unrecognized"

            # Displaying summary
            print("\nSummary:")
            print(f"Item: {matched_item.capitalize()}")
            print(f"Category: {category.capitalize()}")
            print(f"Price: {price}$")
            print(f"Date of Purchase: {formatted_date}")
        else:
            # Item not found in the dataset
            print(f"Unrecognized item: {item.capitalize()}")

            # Ask the user to provide the category for the item
            category = input("Please provide the category for this item: ")

            # Add the new item and category to the dataset
            add_new_item_to_csv(item, category)

            # Display the updated summary
            print("\nSummary:")
            print(f"Item: {item.capitalize()}")
            print(f"Category: {category.capitalize()}")
            print(f"Price: {price}$")
            print(f"Date of Purchase: {formatted_date}")

        another_purchase = input("Do you want to make another purchase? (yes/no): ")
        if another_purchase.lower() != 'yes':
            break

# Example usage:
chatbot()