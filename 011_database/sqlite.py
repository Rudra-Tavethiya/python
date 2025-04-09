
import sqlite3


mydb = sqlite3.connect("data.db")

# mydb.execute("create table student(id int primary key, namr varchar(20), email varchar(50), passsword varchar(8))")

# mydb.execute("insert into student values(1,'rudra','r@gmail.com',123456)")

data = mydb.execute("select * from student")
print(data)


mydb.commit()