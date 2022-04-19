# import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)
mycursor = mydb.cursor()
def READ():
  mycursor.execute("SELECT * FROM employees_table")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  mydb.commit()