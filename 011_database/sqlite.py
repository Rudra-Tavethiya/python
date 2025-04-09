
import sqlite3


mydb = sqlite3.connect("data.db")

# mydb.execute("create table student(id int primary key, namr varchar(20), email varchar(50), passsword varchar(8))")

# mydb.execute("insert into student values(1,'rudra','r@gmail.com',123456)")

# mydb.execute("insert into student values(2,'fenil','f@gmail.com',654321)")

r = mydb.execute("select * from student")
print(r)

# for data in r.fetchall():
#     print(data)

for data in r.fetchall():
    for i in data:
        print(i,end="   ")
    print()

mydb.commit()