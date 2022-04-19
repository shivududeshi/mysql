import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()


sql = "UPDATE customers_table SET name = %s WHERE phone_no = %s"
val = ("shiva", "9342348002")
mycursor.execute(sql, val)

mydb.commit()