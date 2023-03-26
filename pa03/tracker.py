#! /opt/miniconda3/bin/python3
'''
Create a file tracker.py which offers the user the following options and makes calls to the Transaction class to update the database.

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

The tracker.py program should not have any SQL calls and should be similar is structure to the todo2.py program from Lesson19.

todo2.py code for reference:
todo2 is an app that maintains a todo list
just as with the todo code in this folder.

but it also uses an Object Relational Mapping (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, TodoList, will map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:

(5,'commute','drive to work',false) <-->

{rowid:5,
 title:'commute',
 desc:'drive to work',
 completed:false)
 }

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/todo.db

Recall that sys.argv is a list of strings capturing the
command line invocation of this program
sys.argv[0] is the name of the script invoked from the shell
sys.argv[1:] is the rest of the arguments (after arg expansion!)

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''
from transaction import Transaction

class Tracker:
    ''' Constructor for Tracker. Will also take in a database file to parse information from. '''
    def __init__(self, db_file):
        self.db_file = db_file
        self.transactions = Transaction(db_file)
    
    ''' Will display the menu options at the start and take in user input choice. Depending on the number input, it will process their request. '''
    def run(self):
        print("Welcome to your finance tracker!")
        self.print_menu()
        while True:
            choice = input("\nEnter choice: ")
            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                self.show_categories()
            elif choice == "2":
                self.add_category()
            elif choice == "3":
                self.modify_category()
            elif choice == "4":
                self.show_transactions()
            elif choice == "5":
                self.add_transaction()
            elif choice == "6":
                self.delete_transaction()
            elif choice == "7":
                self.summarize_by_date()
            elif choice == "8":
                self.summarize_by_month()
            elif choice == "9":
                self.summarize_by_year()
            elif choice == "10":
                self.summarize_by_category()
            elif choice == "11":
                self.print_menu()
            else:
                print("Invalid choice, please try again.")
    
    '''will display menu contents'''
    def print_menu(self):
        print("\nPlease choose from the following options:")
        print("0. Quit")
        print("1. Show categories")
        print("2. Add category")
        print("3. Modify category")
        print("4. Show transactions")
        print("5. Add transaction")
        print("6. Delete transaction")
        print("7. Summarize transactions by date")
        print("8. Summarize transactions by month")
        print("9. Summarize transactions by year")
        print("10. Summarize transactions by category")
        print("11. Print this menu")
    
    
    def show_categories(self):
        categories = self.transactions.get_categories()
        if not categories:
            print("No categories found.")
        else:
            print("Categories:")
            for category in categories:
                print(category)
    
    def add_category(self):
        category = input("Enter new category name: ")
        if self.transactions.add_category(category):
            print(f"Added category {category}.")
        else:
            print(f"Failed to add category {category}.")
    
    def modify_category(self):
        old_category = input("Enter category to modify: ")
        new_category = input("Enter new category name: ")
        if self.transactions.modify_category(old_category, new_category):
            print(f"Modified category {old_category} to {new_category}.")
        else:
            print(f"Failed to modify category {old_category}.")
    
    def show_transactions(self):
        transactions = self.transactions.get_transactions()
        if not transactions:
            print("No transactions found.")
        else:
            print("Transactions:")
            for t in transactions:
                print(t)
    
    def add_transaction(self):
        item = input("Enter item name: ")
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        date = input("Enter date (yyyy-mm-dd): ")
        description = input("Enter description: ")
        if self.transactions.add_transaction(item, amount, category, date, description):
            print("Transaction added successfully.")
        else:
            print("Failed to add transaction.")
    
    def delete_transaction(self):
        id = input("Enter transaction id: ")
        if self.transactions.delete_transaction(id):
            print(f"Deleted transaction {id}.")
        else:
            print(f"Failed to delete transaction {id}.")
    
    def summarize_by_date(self):
        summary = self.transactions.summarize_by_date()
        if not summary:
            print("No transactions found.")
        else:
            for row in summary:
                print(row[0], "-", row[1])


    def summarize_by_month(self):
        summary = self.transactions.summarize_by_month()
        if not summary:
            print("No transactions found.")
        else:
            for month, total in summary.items():
                print(f"{month}: ${total:.2f}")


    def summarize_by_year(self):
        summary = self.transactions.summarize_by_year()
        if not summary:
            print("No transactions found.")
        else:
            for year, total in summary.items():
                print(f"{year}: ${total:.2f}")


    def summarize_by_category(self):
        categories = self.transactions.get_categories()
        if not categories:
            print("No categories found.")
            return

        print("Select a category:")
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")

        while True:
            try:
                choice = int(
                    input("Enter choice (1-{}): ".format(len(categories))))
                if choice < 1 or choice > len(categories):
                    raise ValueError
                break
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and {}.".format(
                    len(categories)))

        summary = self.transactions.summarize_by_category(categories[choice-1])
        if not summary:
            print("No transactions found for category {}.".format(
                categories[choice-1]))
        else:
            for month, total in summary.items():
                print(f"{month}: ${total:.2f}")

if __name__ == "__main__":
    tracker = Tracker("trackFinance.db")
    tracker.run()
