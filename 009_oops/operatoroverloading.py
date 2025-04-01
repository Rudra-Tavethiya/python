
class P:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,obj):
        return self.a+obj.a,self.b+obj.b
    
    def __mul__(self,obj):
        return self.a*obj.a,self.b*obj.b

p1 = P(10,50)
p2 = P(20,30)

c=p1*p2
print(c)