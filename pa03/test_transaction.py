''' 
Testing for the methods of the Transaction class.
'''

import pytest
import os
from transaction import Transaction


@pytest.fixture
def transaction():
    return Transaction(':memory:')


def test_create_table(transaction):
    transaction.create_table()
    cursor = transaction.conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='transactions'")
    assert cursor.fetchone()[0] == 'transactions'


def test_add_transaction(transaction):
    transaction.add_transaction(
        'item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    cursor = transaction.conn.execute("SELECT * FROM transactions")
    result = cursor.fetchone()
    assert result[1] == 'item123'
    assert result[2] == 12.34
    assert result[3] == 'Food'
    assert result[4] == '2022-03-26'
    assert result[5] == 'Bought groceries'


def test_delete_transaction(transaction):
    transaction.add_transaction(
        'item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    transaction.delete_transaction(1)
    cursor = transaction.conn.execute("SELECT * FROM transactions")
    result = cursor.fetchone()
    assert result is None


def test_add_category(transaction):
    assert transaction.add_category('Food')

def test_modify_category(transaction):
    transaction.add_category('Food')
    transaction.modify_category('Food', 'Groceries')
    cursor = transaction.conn.execute(
        "SELECT * FROM categories WHERE category='Groceries'")
    result = cursor.fetchone()
    assert result[1] == 'Groceries'


def test_get_category_id(transaction):
    transaction.add_category('Food')
    assert transaction.get_category_id('Food') == None


def test_get_transactions(transaction):
    transaction.add_transaction(
        'item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    transaction.add_transaction(
        'item456', 56.78, 'Clothing', '2022-03-27', 'Bought a shirt')
    transactions = transaction.get_transactions()
    assert len(transactions) == 2


def test_get_categories(transaction):
    transaction.add_transaction(
        'item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    transaction.add_transaction(
        'item456', 56.78, 'Clothing', '2022-03-27', 'Bought a shirt')
    transaction.add_category('Dog')
    assert transaction.get_categories() == ['Clothing', 'Dog', 'Food']
   


def test_summarize_by_date(transaction):
    transaction.add_transaction(
        'item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    transaction.add_transaction(
        'item456', 56.78, 'Clothing', '2022-03-27', 'Bought a shirt')
    summary = transaction.summarize_by_date()
    assert len(summary) == 2
    assert summary[0][0] == '2022-03-26'
    assert summary[0][1] == 12.34
    assert summary[1][0] == '2022-03-27'
    assert summary[1][1] == 56.78


def test_summarize_by_month(transaction):
    transaction.add_transaction('item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    transaction.add_transaction('item456', 56.78, 'Clothing', '2022-04-27', 'Bought a new shirt')
    transaction.add_transaction('item789', 90.12, 'Food', '2022-04-29', 'Bought dinner')
    transaction.add_transaction('itemabc', 34.56, 'Transportation', '2022-05-05', 'Took a taxi')
    result = transaction.summarize_by_month()
    assert result == [('2022-03', 12.34),('2022-04', 146.9), ('2022-05', 34.56)]


def test_summarize_by_year(transaction):
    transaction.add_transaction(
        'item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    transaction.add_transaction(
        'item456', 56.78, 'Clothing', '2022-04-27', 'Bought a new shirt')
    transaction.add_transaction(
        'item789', 90.12, 'Transportation', '2021-05-28', 'Filled up gas tank')
    result = transaction.summarize_by_year()
    assert len(result) == 2
    assert result[0] == ('2021', 90.12)
    assert result[1] == ('2022', 69.12)


def test_summarize_by_category(transaction):
    transaction.add_transaction('item123', 12.34, 'Food', '2022-03-26', 'Bought groceries')
    transaction.add_transaction('item456', 56.78, 'Clothing', '2022-04-27', 'Bought a new shirt')
    transaction.add_transaction('item789', 90.12, 'Transportation', '2021-05-28', 'Filled up gas tank')
    result = transaction.summarize_by_category()
    assert len(result) == 3
    assert result[0] == ('Clothing', 56.78)
    assert result[1] == ('Food', 12.34)
    assert result[2] == ('Transportation', 90.12)
