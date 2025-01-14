from dataclasses import dataclass

@dataclass
class Expenses:
    expense_name: str
    expense_category: str
    expense_price: int

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        if expense:
            self.expenses.append(expense)
            print('Expense Added')

        else:
            print('Add valid expense')

    def view_expense_by_category(self, category):
        if category:
            if not self.expenses:
                print('There are no expense to view')

            else:
                for expense in self.expenses:
                    if expense.expense_category == category:
                        print(f'Expense name is {expense.expense_name} of category {expense.expense_category} of price {expense.expense_price}')

                else:
                    print('Enter Valid Category')
        else:
            print('Enter Category type')

def main():
    expense_tracker = ExpenseTracker()

    while True:

        print('\n1. add expense')
        print('2. view expense')

        option = input("Enter here: ")

        if option == '1':
            expense_name = input('Enter Expense Name: ')
            expense_category = input('Enter Expense Category: ')
            expense_price = input('Enter Expense Price: ')

            expense = Expenses(expense_name, expense_category, expense_price)

            expense_tracker.add_expense(expense)

        elif option == '2':
            category = input('Enter expense category to view: ')

            expense_tracker.view_expense_by_category(category)


if __name__ == '__main__':
    main()
