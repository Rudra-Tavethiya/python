class write:

    id = 101
    name = "python"
    def display(self):
        print("display calling....",self.id)

    def show(self):
        print("show calling....",self.name)

w = write()

w.display()
w.show()