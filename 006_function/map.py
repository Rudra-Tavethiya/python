# map 

# def squre(a):
#     b=int(a)
#     return b*b

# l = [10,20,30,40,50]

# l1 = []
# for i in l:
#     k = squre(i)
#     l1.append(k)
# print(l1)

# l1 = map(squre,l)
# print(list(l1))


# l1 = list(map(squre,(input("enter numbers : ").split())))
# print(list(l1))


# lambda

# l = [1,2,3,4,5]
# l1 = map(lambda x:x*x,l)
# print(list(l1))

# a = [10,20,30,40,50,1,3,4,5]
# b = [1,2,3,4,5]

# c  = map(lambda x,y:x+y,a,b)
# print(list(c))

# c = filter(lambda x:x%2!=0,a)
# print(list(c))


# from math import sqrt

data = [1, 4, 6, 8, 9, 10, 12, 16, 81, 23, 36, 48]  
# def isPreSquare(i):
#     return sqrt(i).is_integer()

# k = filter(isPreSquare,data)
# print(list(k))


from functools import reduce

def add(x,y):
    return x*y

c = reduce(add,data)
c = reduce(lambda x,y:x+y,data)
print(c)