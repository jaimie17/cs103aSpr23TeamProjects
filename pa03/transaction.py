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
from typing import List, Tuple
import sqlite3
import os

class Transaction:
    def __init__(self, db_file: str) -> None:
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self) -> None:
        self.conn.execute('''CREATE TABLE IF NOT EXISTS transactions
                            (id INTEGER PRIMARY KEY,
                             item_number TEXT,
                             amount REAL,
                             category TEXT,
                             date TEXT,
                             description TEXT)''')

    def add_transaction(self, item_number: str, amount: float, category: str, date: str, description: str) -> None:
        self.conn.execute(
            "INSERT INTO transactions (item_number, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            (item_number, amount, category, date, description)
        )
        self.conn.commit()

    def delete_transaction(self, item_number: str) -> None:
        # check if item number exists in the table
        cursor = self.conn.execute(f"SELECT item_number FROM transactions WHERE item_number = '{item_number}'")
        result = cursor.fetchone()
        if not result:
            print(
                f"Failed to delete transaction {item_number}. Transaction not found.")
            return
        # delete the transaction if it exists
        self.conn.execute(
            f"DELETE FROM transactions WHERE item_number = '{item_number}'")
        self.conn.commit()
        print(f"Transaction {item_number} deleted successfully.")


    def add_category(self, category: str) -> bool:
       if self.get_category_id(category):
            print("Category already exists")
            return False
       self.conn.execute(
            f"INSERT INTO categories (name) VALUES ('{category}')")
       self.conn.commit()
       print(f"Category {category} added successfully")
       return True
    
    def get_category_id(self, category: str) -> int:
        cursor = self.conn.execute('''CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, category TEXT)''')
        #ALTER TABLE categories ADD COLUMN name TEXT
        result = cursor.fetchone()
        if not result:
            return None
        return result[0]

    def modify_transaction(self, item_number: str, column_name: str, new_value: str) -> None:
        self.conn.execute(
            f"UPDATE transactions SET {column_name} = '{new_value}' WHERE item_number = '{item_number}'")
        self.conn.commit()

    def get_transactions(self) -> List[Tuple]:
        cursor = self.conn.execute("SELECT * FROM transactions")
        return cursor.fetchall()

    def get_categories(self) -> List[str]:
        cursor = self.conn.execute(
            "SELECT DISTINCT category FROM transactions")
        categories = cursor.fetchall()
        return [category[0] for category in categories]

    def summarize_by_date(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT date, SUM(amount) FROM transactions GROUP BY date")
        return cursor.fetchall()

    def summarize_by_month(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT strftime('%Y-%m', date) as month, SUM(amount) FROM transactions GROUP BY month")
        return cursor.fetchall()

    def summarize_by_year(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT strftime('%Y', date) as year, SUM(amount) FROM transactions GROUP BY year")
        return cursor.fetchall()

    def summarize_by_category(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT category, SUM(amount) FROM transactions GROUP BY category")
        return cursor.fetchall()

    def __del__(self) -> None:
        self.conn.close()
