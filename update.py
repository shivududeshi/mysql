import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()

def UPDATE():
  sql = "UPDATE employees_table SET name = %s WHERE id = %s"
  val = ("ramesh", "1")
  mycursor.execute(sql, val)

  mydb.commit()