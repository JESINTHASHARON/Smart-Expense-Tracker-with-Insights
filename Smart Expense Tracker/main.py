from storage import load_data
from analysis import monthly_summary, category_summary, highest_category, show_pie_chart
from expense import Expense
from storage import save_data
from analysis import show_pie_chart

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = Expense(date, category, amount, description)

    data = load_data()
    data.append(expense.to_dict())
    save_data(data)

    print("✅ Added!")

def view_summary():
    month = input("Enter month (YYYY-MM): ")
    data = load_data()

    total = monthly_summary(data, month)
    categories = category_summary(data, month)

    print(f"\nTotal Expense: ₹{total}")
    print("Category Breakdown:", dict(categories))

    if categories:
        print("Highest Spending Category:", highest_category(categories))
        show_pie_chart(categories)

while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        break
    else:
        print("Invalid choice")