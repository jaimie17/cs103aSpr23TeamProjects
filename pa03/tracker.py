#! /opt/miniconda3/bin/python3
'''
Create a file tracker.py which offers the user the following options and makes calls to the Transaction class to update the database.

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

The tracker.py program should not have any SQL calls and should be similar is structure to the todo2.py program from Lesson19.

todo2.py code for reference:
todo2 is an app that maintains a todo list
just as with the todo code in this folder.

but it also uses an Object Relational Mapping (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, TodoList, will map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:

(5,'commute','drive to work',false) <-->

{rowid:5,
 title:'commute',
 desc:'drive to work',
 completed:false)
 }

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/todo.db

Recall that sys.argv is a list of strings capturing the
command line invocation of this program
sys.argv[0] is the name of the script invoked from the shell
sys.argv[1:] is the rest of the arguments (after arg expansion!)

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from todolist import TodoList
import sys


# here are some helper functions ...

def print_menu():
    ''' print an menu of the commands '''
    print('''Commands:
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
            )

def print_todos(todos):
    ''' print the todo items '''
    if len(todos)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-30s %-10s %-10s"%('item #','amount','category','date','description'))
    print('-'*40)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-30s %2d"%values)

# def process_args(arglist):
#     ''' examine args and make appropriate calls to TodoList'''
#     todolist = TodoList()
#     if arglist==[]:
#         print_usage()
#     elif arglist[0]=="show":
#         print_todos(todolist.selectActive())
#     elif arglist[0]=="showall":
#         print_todos(todos = todolist.selectAll())
#     elif arglist[0]=="showcomplete":
#         print_todos(todolist.selectCompleted())
#     elif arglist[0]=='add':
#         if len(arglist)!=3:
#             print_usage()
#         else:
#             todo = {'title':arglist[1],'desc':arglist[2],'completed':0}
#             todolist.add(todo)
#     elif arglist[0]=='complete':
#         if len(arglist)!= 2:
#             print_usage()
#         else:
#             todolist.setComplete(arglist[1])
#     elif arglist[0]=='delete':
#         if len(arglist)!= 2:
#             print_usage()
#         else:
#             todolist.delete(arglist[1])
#     else:
#         print(arglist,"is not implemented")
#         print_usage()
        
        
        
def process_transaction_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    transactions = Transaction()
    if arglist==[]:
        print_menu()
    elif arglist[0]==str(4): #show transactions
        print_money(transactions.show_transactions())


    # elif arglist[0]==str(1): #show categories
    #     print_money(todos = transactions.show_categories())

    #FROM TO DO LIST     
    # elif arglist[0]=="showcomplete":
    #     print_todos(transactions.selectCompleted())


    # elif arglist[0]==str(2): #add categories
    #     if len(arglist)!=3:
    #         print_menu()
    #     else:
    #         todo = {'amount':arglist[1],'category':arglist[2], 'date':arglist[3],'description':0}
    #         transactions.add_category(todo) #change params


    elif arglist[0]==str(5): #add transaction
        if len(arglist)!=3:
            print_menu()
        else:
            todo = {'amount':arglist[1],'category':arglist[2], 'date':arglist[3],'description':0}
            transactions.add_transaction(todo) #change params

    #FROM TO DO LIST
    # elif arglist[0]=='complete':
    #     if len(arglist)!= 2:
    #         print_usage()
    #     else:
    #         transactions.setComplete(arglist[1])


    # elif arglist[0]==str(3): #modify category
    #     if len(arglist)!= 2:
    #         print_menu()
    #     else:
    #         transactions.modify_category(arglist[1])


    elif arglist[0]==str(6): #delete transaction
        if len(arglist)!= 2:
            print_menu()
        else:
            transactions.delete_transaction(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_menu()

def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='5':
                # join everyting after the name as a string
                args = ['5',args[1]," ".join(args[2:])]
            if agrs[0]=='0':
                break;
            process_transaction_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()
