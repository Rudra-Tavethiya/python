from tkinter import *

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9316977670",
    port=3306,
    database="1_fab"
)

cursor = mydb.cursor()

def add_data():

    name = e1.get()
    email = e2.get()
    paswword = e3.get()

    qry = "insert into data values(%s,%s,%s,%s)"
    val = (0,name,email,paswword)

    cursor.execute(qry,val)
    mydb.commit()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

    

root = Tk()
root.geometry("500x500")

# b1 = Button(text="left").pack(side=LEFT)
# b2 = Button(text="right").pack(side=RIGHT)
# b3 = Button(text="top").pack(side=TOP)
# b4 = Button(text="bottom").pack(side=BOTTOM)


# l1 = Label(text="Name").grid(row=1,column=1)
# l2 = Label(text="Email").grid(row=2,column=1)
# l3 = Label(text="Password").grid(row=3,column=1)

# e1 = Entry().grid(row=1,column=2)
# e2 = Entry().grid(row=2,column=2)
# e3 = Entry().grid(row=3,column=2)

# Button(text="Submit").grid(row=4,column=2)



l1 = Label(text="Name").place(x=100,y=100)
l2 = Label(text="Email").place(x=100,y=150)
l3 = Label(text="Password").place(x=100,y=200)

e1 = Entry()
e1.place(x=200,y=100)
e2 = Entry()
e2.place(x=200,y=150)
e3 = Entry()
e3.place(x=200,y=200)

Button(text="Submit",command=add_data).place(x=250,y=250)




root.mainloop()