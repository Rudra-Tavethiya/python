# Write a Python program to demonstrate handling multiple exceptions.



try : 
    a = int(input("enter numerator : "))
    b = int(input("enter denominator : "))
    c = a/b
    print(c)

except ZeroDivisionError:
    print("You Can Not Divide By Zero!!")

except ValueError : 
    print("invalied input!!!, enter only int value")

finally : 
    print("Try Some More Combination!!")