
from mysql_crud import employee

def is_continue():
    """
    Check for continuation of CRUD operations from user

    Args:
        string (str):User input as Y or N

    Returns
        bool: return True for continuation, False for stop.
    """
    flag=input('Do you want to continue? if yes, type "Y" or type "N": ')
    if flag=='Y':
        return True
    if flag=='N':
        return False
    else:
        print('Invalid input')
        return is_continue()

def user_rudi(emp):
    flag=True
    while flag:
        operation=input('Enter operation among <SEARCH>,<UPDATE>,<DELETE>,<INSERT>')
        if operation.upper()=='SEARCH':
            emp.SEARCH()
        elif operation.upper()=='INSERT':
            emp.INSERT()
        elif operation.upper()=='UPDATE':
            emp.UPDATE()
        elif operation.upper()=='DELETE':
            emp.DELETE()
        else:
            print('invalid operation')
            return user_rudi(emp)
        flag=is_continue()

if __name__=='__main__':
    try:
        emp_1=employee()
        user_rudi(emp_1)
    except Exception as e:
        print('Error is:', e)


        
