
# cs103aSpr23TeamProjects
# CS103a Spring 2023 group project:
We are writing SQL queries to perform CRUD operations (Create, Read, Update, Delete) and aggregation(with SQLite3) to practice and devlop automated testing (with pytest). This web application will allow the user to edit, change, modify, and view their financial transactions using functions that help parse the database.

## Motivation: 
Many software projects use SQLite to manage their data and this problem set will give the experience of building such an app.  Another important process in software engineering is the design of automated tests.  This assignment will allow us to practice develoing a suite of tests for our app. There are other database and testing frameworks, but they are all similar in principle and this assignment will expose you to the core concepts and skills you'll need.

### Team Members: 
<br>1. Gianna Everette 
<br>2. Jaimie Louie
<br>3. Samiyanur Islam
<br/>4. Cindy Chi

### Script of Running Pylint:


### Script of Running Pytest:
PS C:\Users\Jaimie\Desktop\cs103aSpr23TeamProjects> python -m pytest -v
====================================== test session starts ======================================
platform win32 -- Python 3.9.13, pytest-7.2.1, pluggy-1.0.0 -- C:\Users\Jaimie\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Jaimie\Desktop\cs103aSpr23TeamProjects
plugins: anyio-3.6.2
collected 12 items

pa03/test_transaction.py::test_create_table PASSED                                         [  8%] 
pa03/test_transaction.py::test_add_transaction PASSED                                      [ 16%] 
pa03/test_transaction.py::test_delete_transaction PASSED                                   [ 25%] 
pa03/test_transaction.py::test_add_category PASSED                                         [ 33%] 
pa03/test_transaction.py::test_modify_category PASSED                                      [ 41%] 
pa03/test_transaction.py::test_get_category_id PASSED                                      [ 50%] 
pa03/test_transaction.py::test_get_transactions PASSED                                     [ 58%] 
pa03/test_transaction.py::test_get_categories PASSED                                       [ 66%] 
pa03/test_transaction.py::test_summarize_by_date PASSED                                    [ 75%] 
pa03/test_transaction.py::test_summarize_by_month PASSED                                   [ 83%] 
pa03/test_transaction.py::test_summarize_by_year PASSED                                    [ 91%] 
pa03/test_transaction.py::test_summarize_by_category PASSED                                [100%] 

====================================== 12 passed in 0.12s =======================================

### Script Running tracker.py:
Welcome to your finance tracker!

Please choose from the following options:
0. Quit
1. Show categories
2. Add category
3. Modify category
4. Show transactions
5. Add transaction
6. Delete transaction
7. Summarize transactions by date
8. Summarize transactions by month
9. Summarize transactions by year
10. Summarize transactions by category
11. Print this menu

Enter choice: 2
Enter new category name: animal
Added category animal.

Enter choice: 5
Enter item name: cat
Enter amount: 30
Enter category: animal2
Enter date (yyyy-mm-dd): 2023-09-09
Enter description: friend
Transaction added successfully.

Enter choice: 1
Categories:   
animal        
animal2       
dog

Enter choice: 4
Transactions:
(1, 'cat', 30.0, 'animal2', '2023-09-09', 'friend')

Enter choice: 6
Enter transaction id: 1
Deleted transaction 1.

Enter choice: 2
Enter new category name: cat
Added category cat.

Enter choice: 5
Enter item name: flower
Enter amount: 20
Enter category: plant
Enter date (yyyy-mm-dd): 2022-03-10
Enter description: plant
Transaction added successfully.

Enter choice: 5
Enter item name: computer
Enter amount: 2222
Enter category: tech
Enter date (yyyy-mm-dd): 1999-03-22
Enter description: broken
Transaction added successfully.

Enter choice: 5
Enter item name: dorm
Enter amount: 22
Enter category: house
Enter date (yyyy-mm-dd): 2021-09-08
Enter description: housing for you
Transaction added successfully.

Enter choice: 4
Transactions:
(1, 'flower', 20.0, 'plant', '2022-03-10', 'plant')
(2, 'computer', 2222.0, 'tech', '1999-03-22', 'broken')
(3, 'dorm', 22.0, 'house', '2021-09-08', 'housing for you')

Enter choice: 7
1999-03-22 - $ 2222.0
2021-09-08 - $ 22.0
2022-03-10 - $ 20.0

Enter choice: 8
1999-03: $2222.00
2021-09: $22.00
2022-03: $20.00

Enter choice: 9
1999: $2222.00
2021: $22.00
2022: $20.00

Enter choice: 10
house: $22.00
plant: $20.00
tech: $2222.00

Enter choice: 0
Goodbye!
