import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()


sql = "DELETE FROM customers_table WHERE phone_no = '9342348000'"
mycursor.execute(sql)

mydb.commit()