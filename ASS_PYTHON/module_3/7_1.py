# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).



# print("single inheritance : ")
# class A:

#     def disp():
#         print("hello")

# class B:

#     def show():
#         print("hello")

# a = A
# a.disp()
# b = B
# b.show()




# print("multiple inheritance : ")
# class A:

#     def run():
#         print("walk...")

# class B:

#     def run():
#         print("runing..")
# class C(A,B):

#     def fast():
#         print("fast runing...")

# c = C
# c.run()
# c.fast()




# class A:

#     def walk():
#         print("walking...")

# class B(A):

#     def run():
#         print("running...")

# class C(B):

#     def fast():
#         print("fast runing...")

# c = C
# c.walk()
# c.run()
# c.fast()




print("multiple inheritance : ")
class A:

    def walk():
        print("walk...")

class B(A):

    def run():
        print("runing..")

class C(A):

    def fast():
        print("fast runing...")
    
class D(B,C):

    def very():
        print("very fast runing...")

d = D
d.walk()
d.run()
d.fast()
d.very()