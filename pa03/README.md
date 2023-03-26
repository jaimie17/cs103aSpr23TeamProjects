
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

### Script of Running Pylint before modifications:
PS C:\Users\Jaimie\Desktop\cs103aSpr23TeamProjects\pa03> python -m pylint transaction.py
************* Module transaction
transaction.py:31:0: C0301: Line too long (115/100) (line-too-long)
transaction.py:33:0: C0301: Line too long (113/100) (line-too-long)
transaction.py:48:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
transaction.py:50:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
transaction.py:52:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
transaction.py:53:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
transaction.py:54:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:64:0: C0301: Line too long (119/100) (line-too-long)
transaction.py:17:0: C0115: Missing class docstring (missing-class-docstring)
transaction.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:31:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:31:4: R0913: Too many arguments (6/5) (too-many-arguments)
transaction.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:38:33: C0103: Argument name "id" doesn't conform to snake_case naming style (invalid-name)
transaction.py:38:33: W0622: Redefining built-in 'id' (redefined-builtin)
transaction.py:41:8: W0612: Unused variable 'result' (unused-variable)
transaction.py:47:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:55:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:63:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:63:30: W0613: Unused argument 'category' (unused-argument)
transaction.py:71:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:81:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:86:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:91:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:96:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:15:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 5.18/10

PS C:\Users\Jaimie\Desktop\cs103aSpr23TeamProjects\pa03> python -m pylint tracker.py
************* Module tracker
tracker.py:2:0: C0301: Line too long (113/100) (line-too-long)
tracker.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:27:70: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:60:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:76:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:77:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:87:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:88:41: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:95:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:96:65: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:103:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:104:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:114:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:125:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:126:45: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:135:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:136:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:142:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:182:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:21:0: W0105: String statement has no effect (pointless-string-statement)
tracker.py:22:0: C0115: Missing class docstring (missing-class-docstring)
tracker.py:27:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:33:12: R1723: Unnecessary "elif" after "break", remove the leading "el" from "elif" (no-else-break)
tracker.py:28:4: R0912: Too many branches (14/12) (too-many-branches)
tracker.py:61:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:62:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:78:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:79:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:88:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:89:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:96:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:97:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:99:11: E1101: Instance of 'Transaction' has no 'get_category' member (no-member)
tracker.py:116:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:117:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:123:16: C0103: Variable name "t" doesn't conform to snake_case naming style (invalid-name)
tracker.py:126:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:127:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:137:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:138:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:139:8: W0622: Redefining built-in 'id' (redefined-builtin)
tracker.py:139:8: C0103: Variable name "id" doesn't conform to snake_case naming style (invalid-name)
tracker.py:143:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:144:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:152:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:153:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:161:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:162:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:170:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:171:4: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:110:12: W0201: Attribute 'categories' defined outside __init__ (attribute-defined-outside-init)

-----------------------------------
Your code has been rated at 5.79/10

### Script of Running Pylint after modifications:
PS C:\Users\Jaimie\Desktop\cs103aSpr23TeamProjects\pa03> python -m pylint transaction.py
************* Module transaction
transaction.py:36:0: C0301: Line too long (115/100) (line-too-long)
transaction.py:42:0: C0301: Line too long (113/100) (line-too-long)
transaction.py:81:0: C0301: Line too long (119/100) (line-too-long)
transaction.py:36:4: R0913: Too many arguments (6/5) (too-many-arguments)
transaction.py:47:33: C0103: Argument name "id" doesn't conform to snake_case naming style (invalid-name)
transaction.py:47:33: W0622: Redefining built-in 'id' (redefined-builtin)
transaction.py:52:8: W0612: Unused variable 'result' (unused-variable)
transaction.py:78:30: W0613: Unused argument 'category' (unused-argument)

------------------------------------------------------------------
Your code has been rated at 8.55/10 (previous run: 5.18/10, +3.37)

PS C:\Users\Jaimie\Desktop\cs103aSpr23TeamProjects\pa03> python -m pylint tracker.py
************* Module tracker
tracker.py:30:4: R0912: Too many branches (14/12) (too-many-branches)
tracker.py:106:11: E1101: Instance of 'Transaction' has no 'get_category' member (no-member)
tracker.py:131:16: C0103: Variable name "t" doesn't conform to snake_case naming style (invalid-name)
tracker.py:148:8: W0622: Redefining built-in 'id' (redefined-builtin)
tracker.py:148:8: C0103: Variable name "id" doesn't conform to snake_case naming style (invalid-name)
tracker.py:118:12: W0201: Attribute 'categories' defined outside __init__ (attribute-defined-outside-init)

------------------------------------------------------------------
Your code has been rated at 9.17/10 (previous run: 5.79/10, +3.38)

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
