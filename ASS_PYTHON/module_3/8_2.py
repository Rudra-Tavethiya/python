# Write Python programs to demonstrate method overriding. 



print("method overriding : ")

class A:

    def show(self):
        print("method A is calling...")

class B(A):

    def show(self):
        print("method B is calling...")

a = A()
b = B()
a.show()
b.show()