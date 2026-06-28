# Daily Expense Tracker System

# List to store all expenses
expenses = []


# Function to add a new expense
def add_expense():

    # Take expense amount from user
    amount = float(input("Enter expense amount: "))

    # Take expense amount from user
    category = input("Enter category: ")

    # Store expense in dictionary
    expense = {
        "amount": amount,
        "category": category
    }

    # Add expense to the list
    expenses.append(expense)
    print("Expense added successfully!")


# Function to view all expenses
def view_expenses():

    # Check if expense list is empty
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\nExpenses:")
         # Display all expenses
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Category: {expense['category']}, Amount: ₹{expense['amount']}")


# Function to calculate total expense
def show_total_expense():

    # Variable to store total
    total = 0

     # Add all expense amounts
    for expense in expenses:
        total += expense["amount"]

    # Display total expense
    print(f"Total Expense: ₹{total}")


# Main menu function
def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expense")
        print("4. Exit")

        # Take user choice
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total_expense()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the program
menu()