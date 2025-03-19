class write:

    id = 101
    name = "python"

    def __init__(self,id,name):
        self.id = id
        self.name = name


    def display(self):
        print("display calling....",self.id)

    def show(self):
        print("show calling....",self.name)

w1 = write(11,"rudra")

w1.display()
w1.show()

w2 = write(12,"hello")

w2.display()
w2.show()
