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
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                            (item_no INTEGER PRIMARY KEY, amount REAL, category TEXT, date TEXT, description TEXT)''')
        self.conn.commit()

    def show_categories(self):
        ''' return a list of all categories'''
        self.cur.execute("SELECT DISTINCT category from transactions")
        return [row[0] for row in self.cur.fetchall()]

    def add_category(self, category):
        ''' create a new category '''
        self.cur.execute("INSERT INTO transactions (category) VALUES (?)", (category,))
        self.conn.commit()

    def modify_category(self, old_category, new_category):
        ''' modify an existing category '''
        self.cur.execute("UPDATE transactions SET category=? WHERE category=?", (new_category, old_category))
        self.conn.commit()

    def show_transactions(self):
        ''' return all of the transactions as a list of dicts.'''
        self.cur.execute("SELECT * from transactions")
        rows = self.cur.fetchall()
        return [toDict(row) for row in rows]

    def add_transaction(self, transaction):
        ''' create a new transaction and add it to the transactions table '''
        self.cur.execute("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)",
                          (transaction['amount'], transaction['category'], transaction['date'], transaction['description']))
        self.conn.commit()

    def delete_transaction(self, item_no):
        ''' delete a transaction '''
        self.cur.execute("DELETE FROM transactions WHERE item_no=?", (item_no,))
        self.conn.commit()

    def summarize_transactions_by_date(self):
        ''' summarize transactions by date '''
        self.cur.execute("SELECT date, SUM(amount) FROM transactions GROUP BY date")
        return self.cur.fetchall()

    def summarize_transactions_by_month(self):
        ''' summarize transactions by month '''
        self.cur.execute("SELECT strftime('%Y-%m', date) as month, SUM(amount) FROM transactions GROUP BY month")
        return self.cur.fetchall()

    def summarize_transactions_by_year(self):
        ''' summarize transactions by year '''
        self.cur.execute("SELECT strftime('%Y', date) as year, SUM(amount) FROM transactions GROUP BY year")
        return self.cur.fetchall()

    def summarize_transactions_by_category(self):
        ''' summarize transactions by category '''
        self.cur.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
        return self.cur.fetchall()

    def runQuery(self, query, params):
        ''' execute an arbitrary SQL query '''
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur.fetchall()
