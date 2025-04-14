# Write Python programs to demonstrate method overloading



print("overloading : ")

class clc:

    # def add(self,a,b):
    #     r = a + b
    #     print("m1 = ",r)

    # def add(self,a,b,c):
    #     r = a + b + c
    #     print("m2 = ",r)

    # def add(self,a,b):
    #     r = a + b
    #     print("m3 = ",r)

    def add(self,*a):
        sum=0
        for i in a:
            sum+=i
        print("result : ",sum)

c = clc()
c.add(5,6,2.2,4)