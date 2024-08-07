filename = "reportt.txt"
def initialize_file():
    with open(filename, "r") as file:
        file.read()
        with open(filename, "w") as file:
            file.write("Date,Category,Amount,Description\n")


def add_expenses(date, category, amount, description):
    with open(filename, "a") as file:
        file.write(f"{date}, {category}, {amount}, {description}\n")
    print("THE EXPENSE IS ADDED SUCCESSFULLY")


def view_expenses():
    with open(filename, "r") as file:
        expenses = file.readlines()
        print("\n all expenses:")
        for expense in expenses:
            category, date, amount, description = expense.strip().split(",")
            print(
                f"date : {date}, category : {category}, amount : {amount}, description : {description}"
            )
        print()


def view_expenses_by_category():
    search = input("Enter the category you want to search and know the expenses: ")
    with open(filename, "r") as file:
        expenses = file.readlines()
        print(f"\nExpenses in category : '{search}' : ")
        for expense in expenses:
            if category == 'search':
                category, date, amount, description = expense.strip().split(",")
                print(
                    f"date : {date}, category : {category}, amount : {amount}, description : {description}"
                )
        print()


def total_expenses():
    total = 0
    with open(filename, "r") as file:
        expenses = file.readlines()
        for expense in expenses:
            category, date, amount, description = expense.strip().split(",")
            total += amount
        print(f"total expenses: {total}")

        print(f"total expenses: {total}")


initialize_file()
while True:
    print("WELCOME TO EXPENSES TRACKER ")
    print(
        """List of operations you can perform
                                    1.Add Expenses with details
                                    2.View expenses by category
                                    3.Display the total expenses
                                    4.View all expenses"""
    )
    choice = input("enter your choice via 1/2/3/4: ")
    if choice == "1":
        date = input("enter the date(dd/mm/yy): ")
        amount = float(input("enter the amount you spend: "))
        category = input("enter the category you spend the money: ")
        description = input("enter the description")
        add_expenses(date, category, amount, description)
    elif choice == "2":
        view_expenses_by_category()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        view_expenses()
    choice2 = input(
        """Do You Want To Perform More Operations
                    'y' for YES 'n' for NO: """
    )
    if choice2 == "n":
        print("THANK YOU FOR USING EXPENSE TRACKER.")
        break
