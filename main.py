import csv

def add_expense():
    expense = input("Add Expense(e.g., Food, Transport): ")
    amount = input("What's the amount spent: ")
    expense_details = [expense,amount]
    with open("expenses.csv","a",newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(expense_details)


def view_expenses():
    with open("expenses.csv","r") as file:
        reader = csv.reader(file)
        for rows in reader:
            expense = rows[0]
            amount = rows[1]
            print(f"{expense} - ${amount}")
            if not rows:
                print("No expenses recorded yet.")


def calculate_spending():
    with open("expenses.csv","r") as file:
        reader = csv.reader(file)
        total_amount = 0
        for rows in reader:
            amount = float(rows[1])
            total_amount += amount
    return total_amount


while True:
    print('''
    Track your Expenses!
    Options:
    1: Add an expense
    2: View you expenses
    3: View you total expenditure
    4: Exit
    
    ''')

    entry = int(input('Choose an option to continue: '))

    if entry == 1:
        add_expense()
    elif entry == 2:
        view_expenses()
    elif entry == 3:
        print(f"Total spending so far: ${calculate_spending():.2f}")
    elif entry == 4:
        print('Done')
        break
    else:
        print('Invalid Entry')




