'''
Testing with pytest -- 
create a file, test_transaction.py, and addtests to it for each method in the Transaction class. 
It is a good idea to add a test each time you implement a feature. 
You are testing the Transaction class, not the tracker.py user interface code.
'''

import pytest
from transaction import Transaction


@pytest.fixture(scope="module")
def transaction():
    return Transaction(":memory:")


def test_add_category(transaction):
    transaction.add_category("Food")
    categories = transaction.get_categories()
    assert "Food" in categories


def test_modify_category(transaction):
    transaction.add_category("Groceries")
    transaction.modify_category("Groceries", "Food")
    categories = transaction.get_categories()
    assert "Groceries" not in categories
    assert "Food" in categories


def test_add_transaction(transaction):
    transaction.add_category("Food")
    transaction.add_transaction("Pizza", 10.50, "Food", "2023-03-25", "Lunch")
    transactions = transaction.get_transactions()
    assert len(transactions) == 1
    assert transactions[0]["item"] == "Pizza"


def test_delete_transaction(transaction):
    transaction.add_category("Food")
    transaction.add_transaction("Pizza", 10.50, "Food", "2023-03-25", "Lunch")
    transaction.delete_transaction(1)
    transactions = transaction.get_transactions()
    assert len(transactions) == 0


def test_summarize_by_date(transaction):
    transaction.add_category("Food")
    transaction.add_transaction("Pizza", 10.50, "Food", "2023-03-25", "Lunch")
    transaction.add_transaction("Sushi", 15.75, "Food", "2023-03-25", "Dinner")
    summary = transaction.summarize_by_date()
    assert summary == {"2023-03-25": 26.25}


def test_summarize_by_month(transaction):
    transaction.add_category("Food")
    transaction.add_transaction("Pizza", 10.50, "Food", "2023-03-25", "Lunch")
    transaction.add_transaction("Sushi", 15.75, "Food", "2023-03-30", "Dinner")
    summary = transaction.summarize_by_month()
    assert summary == {"2023-03": 26.25 + 15.75}


def test_summarize_by_year(transaction):
    transaction.add_category("Food")
    transaction.add_transaction("Pizza", 10.50, "Food", "2023-03-25", "Lunch")
    transaction.add_transaction("Sushi", 15.75, "Food", "2024-03-30", "Dinner")
    summary = transaction.summarize_by_year()
    assert summary == {"2023": 26.25, "2024": 15.75}


def test_summarize_by_category(transaction):
    transaction.add_category("Food")
    transaction.add_transaction("Pizza", 10.50, "Food", "2023-03-25", "Lunch")
    transaction.add_transaction("Sushi", 15.75, "Food", "2023-03-30", "Dinner")
    summary = transaction.summarize_by_category()
    assert summary == {"Food": 26.25 + 15.75}

