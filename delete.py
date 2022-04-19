# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="dny800",
#   database='customer'
# )

# mycursor = mydb.cursor()

def DELETE():
  sql = "DELETE FROM employees_table WHERE id = '7'"
  mycursor.execute(sql)
  mydb.commit()