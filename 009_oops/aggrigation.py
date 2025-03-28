

class A:

    def show(self):
        print("class A is calling...")

class B:
    a=A()


b = B()
b.a.show()