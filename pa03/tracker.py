'''
tracker.py offers the user the following options 
and makes calls to the Transaction class to update the database.

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

'''

from transaction import Transaction

class Tracker:
    '''This class calls the Transaction class to update the database.'''
    def __init__(self, db_file):
        ''' Written by Samiya 
        Initializes the Tracker object and takes in the database file. '''
        self.db_file = db_file
        self.transactions = Transaction(db_file)

    def run(self):
        ''' Written by Samiya
        Takes in user input of a number to run a finances command. '''
        print("Welcome to your finance tracker!")
        self.print_menu()
        while True:
            choice = input("\nEnter choice: ")
            if choice == "0":
                print("Goodbye!")
                break
            if choice == "1":
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

    def print_menu(self):
        ''' Written by Samiya
        prints out the menu to perform various finance commands. '''
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
        ''' Written by Jaimie
        shows the existing categories that the user had inputted. '''
        categories = self.transactions.get_categories()
        if not categories:
            print("No categories found.")
        else:
            print("Categories:")
            for category in categories:
                print(category)

    def add_category(self):
        ''' Written by Jaimie
        adds category to the database '''
        category = input("Enter new category name: ")
        if self.transactions.add_category(category):
            print(f"Added category {category}.")
        else:
            print(f"Failed to add category {category}.")

    def get_category(self):
        ''' Written by Cindy
        returns the category the user inputs in if it exists. '''
        category = input("Enter category name: ")
        if self.transactions.get_category(category):
            print(f"Found category {category}.")
        else:
            print(f"Failed to find category {category}.")


    def modify_category(self):
        ''' Written by Cindy
        modifies the name of an existing category name. '''
        category = input("Enter category to modify: ")
        new_category = input("Enter new category name: ")
        if self.transactions.modify_category(category, new_category):
            self.categories = self.transactions.get_categories()
            print(f"Category {category} modified to {new_category} successfully")
        else:
            print("Failed to modify category")

    def show_transactions(self):
        ''' Written by Gianna
        returns a list of transations the user had inputted. '''
        transactions = self.transactions.get_transactions()
        if not transactions:
            print("No transactions found.")
        else:
            print("Transactions:")
            for t in transactions:
                print(t)

    def add_transaction(self):
        ''' Written by Gianna
        adds a transaction to the database'''
        item = input("Enter item name: ")
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        date = input("Enter date (yyyy-mm-dd): ")
        description = input("Enter description: ")
        self.transactions.add_transaction(item, amount, category, date, description)
        print("Transaction added successfully.")

    def delete_transaction(self):
        ''' Written by Samiya
        deletes a transaction from the database '''
        id = input("Enter transaction id: ")
        self.transactions.delete_transaction(id)
        print(f"Deleted transaction {id}.")

    def summarize_by_date(self):
        ''' Written by Cindy and Samiya
        will summarize the finance transactions by date'''
        summary = self.transactions.summarize_by_date()
        if not summary:
            print("No transactions found.")
        else:
            for row in summary:
                print(row[0], "- $", row[1])

    def summarize_by_month(self):
        ''' Written by Cindy and Gianna
        will summarize the finance transactions by month'''
        summary = self.transactions.summarize_by_month()
        if not summary:
            print("No transactions found.")
        else:
            for month, total in summary:
                print(f"{month}: ${total:.2f}")

    def summarize_by_year(self):
        ''' Written by Gianna
        will summarize the finance transactions by year'''
        summary = self.transactions.summarize_by_year()
        if not summary:
            print("No transactions found.")
        else:
            for year, total in summary:
                print(f"{year}: ${total:.2f}")

    def summarize_by_category(self):
        ''' Written by Gianna
        will summarize the finance transactions by category'''
        summary = self.transactions.summarize_by_category()
        if not summary:
            print("No transactions found.")
        else:
            for month, total in summary:
                print(f"{month}: ${total:.2f}")

if __name__ == "__main__":
    # Written by Samiya
    # will run the main method of the program
    tracker = Tracker("finance.db")
    tracker.run()
