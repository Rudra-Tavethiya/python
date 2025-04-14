

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "9316977670",
    port = 3306,
    database = "1_fab"
)


cursor = mydb.cursor()

# cursor.execute("create table data(id int primary key auto_increment, name varchar(20), email varchar(20), paswword varchar(8))")

# cursor.execute("insert into data values(0,'rudra','r@gmail.com','123456')")

# cursor.execute("insert into data values(0,'s','s@gmail.com','159753')")

# cursor.execute("insert into data values(0,'v','v@gmail.com','759846')")





mydb.commit()