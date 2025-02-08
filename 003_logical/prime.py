# n=13
# flag=0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break

# if flag==0:
#     print("prime")
# else:
#     print("not prime")



for i in range(3,101):
    temp=0
    n=i
    for j in range(2,n):
        if n%j==0:
            temp=1
            break

    if temp==0:
        print(n)
        
    