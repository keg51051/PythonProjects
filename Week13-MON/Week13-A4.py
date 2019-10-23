#!C:\Python\python.exe
import mysql.connector
print("Content-Type: text/html \n\n")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="week13"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
mycursor.execute(sql)

mydb.commit()

print("table created.")
