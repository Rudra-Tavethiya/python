# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder. 




marks = int(input("enter the marks out of 100 : "))


if(marks>100 or marks<0):
    print("enter valid marks!!!")
elif marks<=100 and marks>95:
    print("your grade : A+")
elif marks<=95 and marks>90:
    print("your grade : A")
elif marks<=90 and marks>80:
    print("your grade : B+")
elif marks<=80 and marks>70:
    print("your grade : B")
elif marks<=70 and marks>50:
    print("your grade : C+")
elif marks<=50 and marks>=35:
    print("your grade : C")
else :
    print("you are FAIL !!!!")