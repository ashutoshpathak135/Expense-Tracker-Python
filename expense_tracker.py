import json
import os

FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add expense
def add_expense(expenses):
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# View all expenses
def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- All Expenses -----")

    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            expense["name"],
            "-",
            expense["category"],
            "- ₹",
            expense["amount"]
        )


# Calculate total
def total_expense(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expense: ₹", total)


# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)

    if len(expenses) == 0:
        return

    number = int(input("\nEnter expense number to delete: "))

    if 1 <= number <= len(expenses):
        deleted = expenses.pop(number - 1)
        save_expenses(expenses)

        print(deleted["name"], "deleted successfully!")
    else:
        print("Invalid expense number.")


# Main program
expenses = load_expenses()

while True:
    print("\n========================")
    print("      EXPENSE TRACKER")
    print("========================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_expense(expenses)

    elif choice == "4":
        delete_expense(expenses)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")