import mysql.connector
class employee():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dny800",
    database='customer'
    )
    mycursor = mydb.cursor()

    def DELETE(self):
        id_val=int(input('Enter the id to delete: '))
        sql = f"DELETE FROM employees_table WHERE id ={id_val} "
        self.mycursor.execute(sql)
        self.mydb.commit()


    def UPDATE(self):
        print('columns in table: <id>,<name>,<phone_no>,<city>,<joined_date>')
        val =list(input('Enter update details in the format: <id>,<column to update>,<value to update>').split(','))
        sql = f"UPDATE employees_table SET {val[1]} = '{val[2]}' WHERE id = {val[0]}"
        self.mycursor.execute(sql)
        self.mydb.commit()


    def SEARCH(self):
        print('columns in table: <id>,<name>,<phone_no>,<city>,<joined_date>')
        column =input('Enter the column to search for: ')
        sql=''
        if column in ['name','city']:
            pattern =list(input('Enter the pattern in format:<startswith/endswith/contains>,<char to search> ').split(','))
            if pattern[0]=='startswith':
                pat=pattern[1]+'%'
                sql=f"SELECT * FROM employees_table WHERE {column} LIKE '{pat}'"
            elif pattern[0]=='endswith':
                pat='%'+pattern[1]
                sql=f"SELECT * FROM employees_table WHERE {column} LIKE '{pat}'"
            elif pattern[0]=='contains':
                pat='%'+pattern[1]+'%'
                sql=f"SELECT * FROM employees_table WHERE {column} LIKE '{pat}'"

        elif column in ['id','phone_no']:
            pattern =input('Enter the pattern in format:<after/before/in-between>,<numner to search> ').split(',')
            if pattern[0]=='before':
                sql=f"SELECT * FROM employees_table WHERE {column}<{pattern[1]}"
            elif pattern[0]=='after':
                sql=f"SELECT * FROM employees_table WHERE {column}>{pattern[1]}"
            elif pattern[0]=='in-between':
                value1=min(int(pattern[1]),int(pattern[2]))
                value2=max(int(pattern[1]),int(pattern[2]))
                sql=f"SELECT * FROM employees_table WHERE {column} BETWEEN '{value1}' AND '{value2}' "
        
        elif column=='joined_date':
            pattern =input('Enter the pattern in format:<after/before/in-between>,<numner to search> ').split(',')
            if pattern[0]=='before':
                sql=f"SELECT * FROM employees_table WHERE DATE({column})<'{pattern[1]}'"
            elif pattern[0]=='after':
                sql=f"SELECT * FROM employees_table WHERE DATE({column})>'{pattern[1]}'"
            elif pattern[0]=='in-between':
                sql=f"SELECT * FROM employees_table WHERE DATE({column}) BETWEEN '{pattern[1]}' AND '{pattern[2]}' "
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

    def INSERT(self):
        sql = "INSERT INTO employees_table (name, phone_no,city,joined_date) VALUES(%s,%s,%s,%s)"
        val=list(input('Enter <NAME>,<PHONE_NO>,<CITY>,<JOINED_DATE>').split(','))
        self.mycursor.execute(sql,val)
        self.mydb.commit()
