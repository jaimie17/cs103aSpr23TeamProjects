'''
Transaction should be similar to the Todolist ORM from Lesson 19 in class. It will allow the user to read and update the database as need.
The transaction class should not do any printing!! 
It should have an __init__ method where you pass in the filename for the database to be used (e.g. tracker.db) 
and each transaction should have the following fields stored in a SQL table called transactions.

'item #',
'amount',
'category',
'date',
'description'

todolist.py code for reference:
todolist.py is an Object Relational Mapping to the todolist database

The ORM will work map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:

(5,'commute','drive to work',false) <-->
{rowid:5,title:'commute',desc:'drive to work',completed:false)

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/todo.db

'''
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'item #':t[1], 'amount':t[2], 'category':t[3], 'date':t[4], 'description':t[5]}
    return todo

class Transaction():
    def __init__(self):
        ''' create a connection to the database '''
        self.runQuery('''CREATE TABLE transactions
                    (item_no INTEGER PRIMARY KEY, amount REAL, category TEXT, date TEXT, description TEXT)''')

    def show_categories(self):
        ''' returns a list of all categories in the database'''
        return self.runQuery("SELECT DISTINCT category from transactions")

    def add_category(self, category):
        ''' creates a new category '''
        return self.runQuery("INSERT INTO transactions (category) VALUES (?)", (category,))

    def modify_category(self, old_category, new_category):
        ''' modify an existing category '''
        return self.runQuery("UPDATE transactions SET category=? WHERE category=?", (new_category, old_category))

    def show_transactions(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.runQuery("SELECT * from transactions")

    def add_transaction(self, transaction):
        ''' creates a new transaction and adds it to the transactions table '''
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)",
                          (transaction['amount'], transaction['category'], transaction['date'], transaction['description']))

    def delete_transaction(self, item_no):
        ''' deletes a transaction from the database '''
        return self.runQuery("DELETE FROM transactions WHERE item_no=?", (item_no,))

    def summarize_transactions_by_date(self):
        ''' summarize the transactions by date '''
        return self.runQuery("SELECT date, SUM(amount) FROM transactions GROUP BY date")


    def summarize_transactions_by_month(self):
        ''' summarize the transactions by month '''
        return self.runQuery("SELECT strftime('%Y-%m', date) as month, SUM(amount) FROM transactions GROUP BY month")

    def summarize_transactions_by_year(self):
        ''' summarize the transactions by year '''
        return self.runQuery("SELECT strftime('%Y', date) as year, SUM(amount) FROM transactions GROUP BY year")

    def summarize_transactions_by_category(self):
        ''' summarize the transactions by category '''
        return self.runQuery("SELECT category, SUM(amount) FROM transactions GROUP BY category")

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
