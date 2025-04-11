

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9316977670",
    port=3306,
    database="1_fab"
)

cursor = mydb.cursor()

cursor.execute("select * from student")