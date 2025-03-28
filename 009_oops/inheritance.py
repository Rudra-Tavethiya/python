
# class A:
    
#     _a = 10
#     def disp(self):
#         print("class A calling...",self._a)

# class B(A):

#     def show(self):
#         print("class B calling...",self._a)


# a=A()
# b=B()
# _a=20
# b.show()


# class sample:
    
#     # def __init__(self,a,b):
#         # self.a=a
#         # self.b=b

#     def __init__(self,*a):
#         self.a=a[0]
#         self.b=a[1]

#     def disp(self):
#         print(self.a,self.b)


# s=sample(10,20)

# s.disp()



class A:

    def __init__(self):
        print("class A is calling...")


class B(A):

    def __init__(self):
        print("class B is calling...")
        super().__init__()

b = B()