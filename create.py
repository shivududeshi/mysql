import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dny800",
  database='customer'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employees_table(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone_no BIGINT, city VARCHAR(255) )")

mydb.commit()