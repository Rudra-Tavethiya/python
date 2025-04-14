# Write a Python program to create a class and access its properties using an object.




class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def disp(self):

        print("name : ",self.name)
        print("age : ",self.age)



s = student("r",20)

print("using object : ")
print("name : ",s.name)
print("age : ",s.age)


print("using properties : ")
s.disp()