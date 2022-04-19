import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()

sql="SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'employees_table'"
print(mycursor.execute(sql))

# def INSERT():
#   sql = "INSERT INTO employees_table (name, phone_no,city,joined_date) VALUES(%s,%s,%s,%s)"
#   val=input('Enter <NAME>,<PHONE_NO>,<CITY>,<JOINED_DATE>')
#   mycursor.execute(sql,val)
#   mydb.commit()