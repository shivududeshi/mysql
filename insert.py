import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()


def INSERT():
  sql = "INSERT INTO employees_table (name, phone_no,city,joined_date) VALUES(%s,%s,%s,%s)"
  val=input('Enter <NAME>,<PHONE_NO>,<CITY>,<JOINED_DATE>')
  mycursor.execute(sql,val)
  mydb.commit()