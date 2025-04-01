
from multipledispatch import dispatch

class clc:

    # @dispatch(int,int)
    # def add(self,a,b):
    #     r = a + b
    #     print("m1 = ",r)

    # @dispatch(int,int,int)
    # def add(self,a,b,c):
    #     r = a + b + c
    #     print("m2 = ",r)

    # @dispatch(float,float)
    # def add(self,a,b):
    #     r = a + b
    #     print("m3 = ",r)

    def add(self,*a):
        sum = 0
        for i in a:
            sum+=i
        print("sum : ",sum)

c = clc()
c.add(10,50,20.63)