# PERSONAL EXPENSE TRACKER
# FY B.Tech Python Mini Project

from datetime import datetime

expenses = []

print("=" * 45)
print("          PERSONAL EXPENSE TRACKER")
print("=" * 45)

while True:
    print("\nMAIN MENU")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View category-wise spending")
    print("5. Save expense report")
    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        category = input("Enter category (Food, Travel, Study, Shopping, Other): ").strip().title()
        description = input("Enter expense description: ").strip()

        try:
            amount = float(input("Enter amount in Rs.: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if not category or not description or amount <= 0:
            print("Please enter valid details and an amount greater than zero.")
            continue

        date = datetime.now().strftime("%d-%m-%Y")
        expenses.append({
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nALL EXPENSES")
            print("-" * 65)
            for number, expense in enumerate(expenses, start=1):
                print(
                    f"{number}. {expense['date']} | {expense['category']} | "
                    f"{expense['description']} | Rs. {expense['amount']:.2f}"
                )

    elif choice == 3:
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal spending: Rs. {total:.2f}")
        print("Number of expenses:", len(expenses))

    elif choice == 4:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            category_totals = {}
            for expense in expenses:
                category = expense["category"]
                category_totals[category] = (
                    category_totals.get(category, 0) + expense["amount"]
                )

            print("\nCATEGORY-WISE SPENDING")
            print("-" * 35)
            for category, amount in category_totals.items():
                print(f"{category}: Rs. {amount:.2f}")

    elif choice == 5:
        filename = "expense_report.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write("PERSONAL EXPENSE REPORT\n")
            file.write(
                "Generated: "
                + datetime.now().strftime("%d-%m-%Y %H:%M")
                + "\n"
            )
            file.write("=" * 55 + "\n")

            for expense in expenses:
                file.write(
                    f"{expense['date']} | {expense['category']} | "
                    f"{expense['description']} | Rs. {expense['amount']:.2f}\n"
                )

            total = sum(expense["amount"] for expense in expenses)
            file.write("-" * 55 + "\n")
            file.write(f"TOTAL SPENDING: Rs. {total:.2f}\n")

        print("Report saved successfully as", filename)

    elif choice == 0:
        print("Thank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
