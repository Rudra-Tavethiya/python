# age=23
# if age>=18:
#     print("elegeble for wvote ")
# else :
#     print("not elegeble for vote")



# a = 100
# b = 100
# c = 50

# if a>b:
#     if a>c:
#         print("A is greater")
#     else:
#         print("C is greater")
# else:
#     if b>c:
#         print("B is greater")
#     else:
#         print("C is greater")


# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is greater")
# elif c>a and c>b:
#     print("C is greater")
# else:
#     print("any two are same")



a = int(input("enter number a : "))
b = int(input("Enter number b : "))

c = int(input("""Enter choice : 
        1 : Add
        2 : sub
        3 : Mul
        4 : div
"""))

if c ==1:
    print("Addition is : ",(a+b))
elif c==2:
    print("substraction is : ",(a-b))
elif c==3:
    print("multiplication is : ",(a*b))
elif c==4:
    print("division is : ",(a/b))
else:
    print("Invalid choice")