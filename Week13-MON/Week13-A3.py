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

sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")