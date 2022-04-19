
def DELETE(mycursor):
    id_val=int(input('Enter the id to delete: '))
    sql = f"DELETE FROM employees_table WHERE id ={id_val} "
    mycursor.execute(sql)

def UPDATE(mycursor):
    print('columns in table: <id>,<name>,<phone_no>,<city>,<joined_date>')
    val =list(input('Enter update details in the format: <id>,<column to update>,<value to update>').split(','))
    sql = f"UPDATE employees_table SET {val[1]} = '{val[2]}' WHERE id = {val[0]}"
    mycursor.execute(sql)


def SEARCH(mycursor):
    print('columns in table: <id>,<name>,<phone_no>,<city>,<joined_date>')
    column =input('Enter the column to search for: ')
    if column in ['name','city']:
        pattern =list(input('Enter the pattern in format:<startswith/endswith/contains>,<char to search> ').split(','))
        if pattern[0]=='startswith':
            pat=pattern[1]+'%'
            sql=f"SELECT * FROM employees_table WHERE '{column}' LIKE '{pat}'"
        elif pattern[0]=='endswith':
            pat='%'+pattern[1]
            sql="SELECT * FROM employees_table WHERE '{column}' LIKE '{pat}'"
        elif pattern[0]=='contains':
            pat='%'+pattern[1]+'%'
            sql="SELECT * FROM employees_table WHERE '{column}' LIKE '{pat}'"

    elif column in ['id','phone_no']:
        pattern =input('Enter the pattern in format:<after/before/in-between>,<char to search> ').split(',')
        if pattern[0]=='before':
            sql="SELECT * FROM employees_table WHERE '{column}'<'{pattern[1]}'"
        elif pattern[0]=='after':
            sql="SELECT * FROM employees_table WHERE '{column}'>'{pattern[1]}'"
        # elif pattern[0]=='in-between':
        #     sql="SELECT * FROM employees_table WHERE '{column}' between "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    # mydb.commit()

    # elif column=='joined_date':
    #     pass

def INSERT(mycursor):
  sql = "INSERT INTO employees_table (name, phone_no,city,joined_date) VALUES(%s,%s,%s,%s)"
  val=list(input('Enter <NAME>,<PHONE_NO>,<CITY>,<JOINED_DATE>').split(','))
  mycursor.execute(sql,val)
  