import sqlite3
import os

def toDict(t):
    ''' t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'item #':t[1], 'amount':t[2], 'category':t[3], 'date':t[4], 'description':t[5]}
    return todo

class Transaction():
    def __init__(self, db_file):
        self.db_file = db_file
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item # int, amount real, category text, date text, description text)''',())

    def show_categories(self):
        ''' return a list of all categories'''
        return self.runQuery("SELECT DISTINCT category from transactions",())

    def add_category(self, category):
        ''' create a new category '''
        return self.runQuery("INSERT INTO transactions (category) VALUES (?)",(category,))

    def modify_category(self, old_category, new_category):
        ''' modify an existing category '''
        return self.runQuery("UPDATE transactions SET category=? WHERE category=?", (new_category, old_category))

    def show_transactions(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.runQuery("SELECT * from transactions",())

    def add_transaction(self, transaction):
        ''' create a new transaction and add it to the transactions table '''
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)",
                             (transaction['amount'], transaction['category'], transaction['date'], transaction['description']))

    def delete_transaction(self, item_no):
        ''' delete a transaction '''
        return self.runQuery("DELETE FROM transactions WHERE item_no=?", (item_no,))

    def summarize_transactions_by_date(self):
        ''' summarize transactions by date '''
        return self.runQuery("SELECT date, SUM(amount) FROM transactions GROUP BY date",())

    def summarize_transactions_by_month(self):
        ''' summarize transactions by month '''
        return self.runQuery("SELECT strftime('%Y-%m', date) as month, SUM(amount) FROM transactions GROUP BY month",())

    def summarize_transactions_by_year(self):
        ''' summarize transactions by year '''
        return self.runQuery("SELECT strftime('%Y', date) as year, SUM(amount) FROM transactions GROUP BY year",())

    def summarize_transactions_by_category(self):
        ''' summarize transactions by category '''
        return self.runQuery("SELECT category, SUM(amount) FROM transactions GROUP BY category",())

    def print_menu(self):
        ''' print the menu options '''
        menu = '''Menu:'''
