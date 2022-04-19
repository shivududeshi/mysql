import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()

#insert

# sql = "INSERT INTO customers_table (name, phone_no) VALUES(%s,%s)"
# val=('ramesh','9342348574')
# mycursor.execute(sql,val)

#update

# sql = "UPDATE customers_table SET phone_no = %s WHERE phone_no = %s"
# val = ("9342348590", "9342348574")
# mycursor.execute(sql, val)

#delete

# sql = "DELETE FROM customers_table WHERE phone_no = '9342348577'"
# mycursor.execute(sql)

#read

mycursor.execute("SELECT * FROM customers_table")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mydb.commit()
