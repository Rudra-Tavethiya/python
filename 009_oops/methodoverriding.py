

class A:

    def show(self):
        print("method A is calling...")

class B(A):

    def show(self):
        print("method B is caling...")


b = B()
b.show()