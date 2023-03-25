'''
Testing with pytest -- 
create a file, test_transaction.py, and addtests to it for each method in the Transaction class. 
It is a good idea to add a test each time you implement a feature. 
You are testing the Transaction class, not the tracker.py user interface code.
'''

import unittest
import sqlite3
from transaction import Transaction


class TestTransaction(unittest.TestCase):
    def setUp(self):
        # create an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')
        self.transaction = Transaction(db_file=self.conn)

    def tearDown(self):
        # close the database connection after testing
        self.conn.close()

    def test_show_categories(self):
        # add some categories to the database
        self.transaction.add_category('food')
        self.transaction.add_category('transportation')
        self.transaction.add_category('entertainment')

        # test if the show_categories method returns the correct list of categories
        self.assertEqual(self.transaction.show_categories(), [
                         ('food',), ('transportation',), ('entertainment',)])

    def test_add_category(self):
        # add a category to the database
        self.transaction.add_category('food')

        # test if the category has been added successfully
        self.assertEqual(self.transaction.show_categories(), [('food',)])

    def test_modify_category(self):
        # add a category to the database
        self.transaction.add_category('food')

        # modify the category to 'groceries'
        self.transaction.modify_category('food', 'groceries')

        # test if the category has been modified successfully
        self.assertEqual(self.transaction.show_categories(), [('groceries',)])

    def test_show_transactions(self):
        # add some transactions to the database
        self.transaction.add_transaction(
            {'amount': 10.5, 'category': 'food', 'date': '2022-01-01', 'description': 'groceries'})
        self.transaction.add_transaction(
            {'amount': 20.0, 'category': 'transportation', 'date': '2022-01-02', 'description': 'gas'})

        # test if the show_transactions method returns the correct list of transactions
        self.assertEqual(self.transaction.show_transactions(), [
                         (1, 10.5, 'food', '2022-01-01', 'groceries'), (2, 20.0, 'transportation', '2022-01-02', 'gas')])

    def test_add_transaction(self):
        # add a transaction to the database
        self.transaction.add_transaction(
            {'amount': 10.5, 'category': 'food', 'date': '2022-01-01', 'description': 'groceries'})

        # test if the transaction has been added successfully
        self.assertEqual(self.transaction.show_transactions(), [
                         (1, 10.5, 'food', '2022-01-01', 'groceries')])

    def test_delete_transaction(self):
        # add a transaction to the database
        self.transaction.add_transaction(
            {'amount': 10.5, 'category': 'food', 'date': '2022-01-01', 'description': 'groceries'})

        # delete the transaction
        self.transaction.delete_transaction(1)

        # test if the transaction has been deleted successfully
        self.assertEqual(self.transaction.show_transactions(), [])

    def test_summarize_transactions_by_date(self):
        # Add some test transactions
        transaction1 = {'amount': 100.0, 'category': 'food', 'date': '2022-01-01', 'description': 'groceries'}
        transaction2 = {'amount': 50.0, 'category': 'entertainment','date': '2022-01-01', 'description': 'movie'}
        transaction3 = {'amount': 25.0, 'category': 'food','date': '2022-01-02', 'description': 'restaurant'}
        self.transaction.add_transaction(transaction1)
        self.transaction.add_transaction(transaction2)
        self.transaction.add_transaction(transaction3)

        # Call the summarize_transactions_by_date method
        results = self.transaction.summarize_transactions_by_date()

        # Verify that the results are correct
        expected_results = [('2022-01-01', 150.0), ('2022-01-02', 25.0)]
        self.assertEqual(results, expected_results)

    def test_summarize_transactions_by_month(self):
        ''' Test summarize_transactions_by_month method '''
        # Insert test transactions
        self.transaction.insert_transaction("2022-01-01", "test1", 100, "food")
        self.transaction.insert_transaction("2022-01-15", "test2", 200, "entertainment")
        self.transaction.insert_transaction( "2022-02-10", "test3", 50, "transportation")
        self.transaction.insert_transaction("2022-02-20", "test4", 150, "food")
        self.transaction.insert_transaction("2022-03-05", "test5", 75, "entertainment")
        self.transaction.insert_transaction("2022-03-20", "test6", 125, "food")

        # Expected result
        expected_result = [("2022-01", 300.0),
                        ("2022-02", 200.0), ("2022-03", 200.0)]

        # Test the method
        result = self.db.summarize_transactions_by_month()
        self.assertEqual(result, expected_result)


def test_summarize_transactions_by_year(self):
    ''' Test summarize_transactions_by_year method '''
    # Insert test transactions
    self.transaction.insert_transaction("2020-01-01", "test1", 100, "food")
    self.transaction.insert_transaction( "2021-01-15", "test2", 200, "entertainment")
    self.transaction.insert_transaction("2021-02-10", "test3", 50, "transportation")
    self.transaction.insert_transaction("2022-02-20", "test4", 150, "food")

    # Expected result
    expected_result = [("2020", 100.0), ("2021", 250.0), ("2022", 150.0)]

    # Test the method
    result = self.transaction.summarize_transactions_by_year()
    self.assertEqual(result, expected_result)


def test_summarize_transactions_by_category(self):
    ''' Test summarize_transactions_by_category method '''
    # Insert test transactions
    self.transaction.insert_transaction("2022-01-01", "test1", 100, "food")
    self.transaction.insert_transaction( "2022-01-15", "test2", 200, "entertainment")
    self.transaction.insert_transaction("2022-02-10", "test3", 50, "transportation")
    self.transaction.insert_transaction("2022-02-20", "test4", 150, "food")
    self.transaction.insert_transaction("2022-03-05", "test5", 75, "entertainment")
    self.transaction.insert_transaction("2022-03-20", "test6", 125, "food")

    # Expected result
    expected_result = [("food", 375.0), ("entertainment", 275.0), ("transportation", 50.0)]

    # Test the method
    result = self.transaction.summarize_transactions_by_category()
    self.assertEqual(result, expected_result)
