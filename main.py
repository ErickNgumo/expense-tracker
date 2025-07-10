import csv
import datetime
from calendar import month


def choosen_category():
    print('''
    Expense Categories
    1. Food
    2. Transport
    3. Entertainment
    4. Shopping
    5. Saving
    6. Miscellaneous    
    ''')
    category = int(input("Choose Category from the Expense Categories list: "))
    return category

def add_expense():
    while True:
        category = choosen_category()
        if category == 1:
            category = 'Food'
        elif category == 2:
            category = 'Transport'
        elif category == 3:
            category = 'Entertainment'
        elif category == 4:
            category = 'Shopping'
        elif category == 5:
            category = 'Saving'
        elif category == 6:
            category = 'Miscellaneous'
        else:
            print('Invalid Entry')
            break
        expense = input("Add Expense(e.g., Food, Transport): ")
        amount = input("What's the amount spent: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        with open("expenses.csv","r") as file:
            reader = csv.reader(file)
            row_count = 0
            for rows in reader:
                row_count += 1
        row_number = row_count + 1

        expense_details = [row_number, category, expense, amount, date]
        with open("expenses.csv","a",newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(expense_details)
        break


def view_expenses():
    with open("expenses.csv","r") as file:
        reader = csv.reader(file)
        for rows in reader:
            row_number = rows[0]
            category = rows[1]
            expense = rows[2]
            amount = rows[3]
            date = rows[4]
            print(f'{row_number} - {category} - {expense} - {amount} - {date}')
            if not rows:
                print("No expenses recorded yet.")


def filter_category_time():
    chosen_sort = int(input("Check you by Category or Date. Enter 1 to sort by Category and 2 to sort by Date: "))
    if chosen_sort == 1:
        with open("expenses.csv","r") as file:
            reader = csv.reader(file)
            for rows in reader:
                category = rows[1]
                expense = int(rows[3])
                category_expense = 0
                user_category = choosen_category()
                if user_category == 1:
                    if category == 'Food':
                        category_expense += expense
                        print(f'You have spent ${category_expense} on {category}')
                elif user_category == 2:
                    if category == 'Transport':
                        category_expense += expense
                        print(f'You have spent ${category_expense} on {category}')
                elif user_category == 3:
                    if category == 'Entertainment':
                        category_expense += expense
                        print(f'You have spent ${category_expense} on {category}')
                elif user_category == 4:
                    if category == 'Shopping':
                        category_expense += expense
                        print(f'You have spent ${category_expense} on {category}')
                elif user_category == 5:
                    if category == 'Saving':
                        category_expense += expense
                        print(f'You have spent ${category_expense} on {category}')
                elif user_category == 6:
                    if category == 'Miscellaneous':
                        category_expense += expense
                        print(f'You have spent ${category_expense} on {category}')
                break
    elif chosen_sort == 2:
        year = int(input('Enter Year: '))
        month = int(input('Enter Month: '))
        day = int(input('Enter Day: '))
        chosen_date = datetime.date(year, month, day)
        with open("expenses.csv","r") as file:
            reader = csv.reader(file)
            day_expense = 0
            for rows in reader:
                row_date = row_date = datetime.datetime.strptime(rows[4], "%Y-%m-%d").date()
                expense = int(rows[3])

                if chosen_date == row_date:
                    day_expense += expense

            print(f'You spent ${day_expense} on {chosen_date}')
    else:
        print('Invalid Choice!')


def calculate_spending():
    with open("expenses.csv","r") as file:
            reader = csv.reader(file)
            total_amount = 0
            for rows in reader:
                amount = float(rows[3])
                total_amount += amount
            return total_amount

def delete_expense():
    view_expenses()
    row_delete = int(input('Enter the row number of the expense you want to delete: '))
    rows = []
    with open("expenses.csv","r") as infile:
        reader = csv.reader(infile)
        for row in reader:
            row_number = int(row[0])
            if row_number != row_delete:
                rows.append(row)

    with open("expenses.csv","w",newline ='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)
    print("The expense has been deleted!")


while True:
    print('''
    Track your Expenses!
    Options:
    1: Add an expense
    2: View your total expenses
    3: View by category or date
    4: View you total expenditure
    5: Delete an expense
    6: Exit
    
    ''')

    entry = int(input('Choose an option to continue: '))

    if entry == 1:
        add_expense()
    elif entry == 2:
        view_expenses()
    elif entry == 3:
        filter_category_time()
    elif entry == 4:
        print(f"Total spending so far: ${calculate_spending():.2f}")
    elif entry == 5:
        delete_expense()
    elif entry == 6:
        print('Done')
        break
    else:
        print('Invalid Entry')




