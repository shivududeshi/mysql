
def DELETE(mycursor):
    id_val=int(input('Enter the id to delete: '))
    sql = f"DELETE FROM employees_table WHERE id ={id_val} "
    mycursor.execute(sql)

def UPDATE(mycursor):
    print('columns in table: <id>,<name>,<phone_no>,<city>,<joined_date>')
    val =list(input('Enter update details in the format: <id>,<column to update>,<value to update>').split(','))
    sql = f"UPDATE employees_table SET {val[1]} = '{val[2]}' WHERE id = {val[0]}"
    mycursor.execute(sql)


def SEARCH(mycursor,mydb):
    print('columns in table: <id>,<name>,<phone_no>,<city>,<joined_date>')
    column =input('Enter the column to search for: ')
    sql=''
    if column in ['name','city']:
        pattern =list(input('Enter the pattern in format:<startswith/endswith/contains>,<char to search> ').split(','))
        if pattern[0]=='startswith':
            sql=f"SELECT * FROM employees_table WHERE {column} LIKE '{pat}'"
        elif pattern[0]=='endswith':
            pat='%'+pattern[1]
            sql=f"SELECT * FROM employees_table WHERE {column} LIKE '{pat}'"
        elif pattern[0]=='contains':
            pat='%'+pattern[1]+'%'
            sql=f"SELECT * FROM employees_table WHERE {column} LIKE '{pat}'"

    elif column in ['id','phone_no','joined_date']:
        pattern =input('Enter the pattern in format:<after/before/in-between>,<numner to search> ').split(',')
        if pattern[0]=='before':
            sql=f"SELECT * FROM employees_table WHERE {column}<{pattern[1]}"
        elif pattern[0]=='after':
            sql=f"SELECT * FROM employees_table WHERE {column}>{pattern[1]}"
        elif pattern[0]=='in-between':
            value1=min(pattern[1],pattern[2])
            value2=min(pattern[1],pattern[2])
            sql="SELECT * FROM employees_table WHERE id between '{value1}' and '{value2}' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    # elif column=='joined_date':
    #     pass

def INSERT(mycursor):
  sql = "INSERT INTO employees_table (name, phone_no,city,joined_date) VALUES(%s,%s,%s,%s)"
  val=list(input('Enter <NAME>,<PHONE_NO>,<CITY>,<JOINED_DATE>').split(','))
  mycursor.execute(sql,val)
  