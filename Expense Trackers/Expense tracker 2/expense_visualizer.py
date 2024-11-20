import json
from datetime import datetime
import matplotlib.pyplot as plt

expenses = {}

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({'category': category, 'amount': amount})
    print(f"Expense of {amount} added under {category} on {date}.")

def view_expenses():
    filter_category = input("Enter category to filter by (leave blank for all): ").strip()
    for date, records in expenses.items():
        for record in records:
            if filter_category == '' or record['category'] == filter_category:
                print(f"Date: {date}, Category: {record['category']}, Amount: {record['amount']}")

def save_expenses_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved to file.")

def load_expenses_from_file(filename):
    try:
        with open(filename, 'r') as file:
            global expenses
            expenses = json.load(file)
        print("Expenses loaded from file.")
    except FileNotFoundError:
        print("File not found. Starting with an empty expense tracker.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty expense tracker.")

def visualize_expenses():
    categories = {}
    for date, records in expenses.items():
        for record in records:
            if record['category'] in categories:
                categories[record['category']] += record['amount']
            else:
                categories[record['category']] = record['amount']
    plt.bar(categories.keys(), categories.values())
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Expenses by Category')
    plt.show()

def main():
    filename = "expenses.json"
    load_expenses_from_file(filename)
    
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save Expenses")
        print("4. Load Expenses")
        print("5. Visualize Expenses")
        print("6. Exit")
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            save_expenses_to_file(filename)
        elif choice == '4':
            load_expenses_from_file(filename)
        elif choice == '5':
            visualize_expenses()
        elif choice == '6':
            save_expenses_to_file(filename)
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
