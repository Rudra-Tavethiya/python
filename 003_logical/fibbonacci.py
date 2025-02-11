# number=15
# a=0
# b=1
# print(a ,b ,end=" ")
# for i in range(number):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c



# using while loop

number = 15
a = 0
b = 1
i = 1
print(a ,b ,end=" ")
while i<=number:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1