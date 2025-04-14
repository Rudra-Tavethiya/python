# Introduction to exceptions and how to handle them using try, except, and finally.




try : 
    a = 5
    b = 0
    c = a/b
    print(c)

except ZeroDivisionError:
    print("You Can Not Divide By Zero!!")


finally : 
    print("Try Some More Combination!!")