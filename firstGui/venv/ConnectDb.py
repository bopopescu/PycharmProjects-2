import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345678",
  database="order_db"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM custdetail")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)