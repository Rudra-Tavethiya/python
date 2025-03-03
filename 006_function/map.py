# map 

def squre(a):
    b=int(a)
    return b*b

l = [10,20,30,40,50]

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

l = [1,2,3,4,5]
l1 = map(lambda x:x*x,l)
print(list(l1))