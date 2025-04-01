from tkinter import *


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

e1 = Entry().place(x=200,y=100)
e2 = Entry().place(x=200,y=150)
e3 = Entry().place(x=200,y=200)

Button(text="Submit").place(x=250,y=250)




root.mainloop()