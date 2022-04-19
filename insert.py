import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()


sql = "INSERT INTO customers_table (name, phone_no) VALUES(%s,%s)"
val=('shivudu','9342348005')
mycursor.execute(sql,val)

mydb.commit()