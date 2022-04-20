import mysql.connector
from mysql_crud import *

def is_continue():
    flag=input('Do you want to continue? if yes, type "Y" or type "N": ')
    if flag=='Y':
        return True
    if flag=='N':
        return False
    else:
        return is_continue()

def user_rudi(mycursor):
    flag=True
    while flag:
        operation=input('Enter operation among <SEARCH>,<UPDATE>,<DELETE>,<INSERT>')
        if operation.upper()=='SEARCH':
            SEARCH(mycursor)
        elif operation.upper()=='INSERT':
            INSERT(mycursor)
        elif operation.upper()=='UPDATE':
            UPDATE(mycursor)
        elif operation.upper()=='DELETE':
            UPDATE(mycursor)
        else:
            raise Exception('invalid operation')
        mydb.commit()
        flag=is_continue()

if __name__=='__main__':
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dny800",
        database='customer'
        )
        mycursor = mydb.cursor()
        user_rudi(mycursor)
    except Exception as e:
        print('Error is:', e)


        
