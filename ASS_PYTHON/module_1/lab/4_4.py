# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if. 




age = int(input("enter your age : "))

if age>=16:
    if age==16:
        print("we need your parental consent for donate blood")
    else : 
        print("you are eligible to donate blood")
else : 
    print("you are not eligible to donate blood")