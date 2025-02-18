# Practical Example 6: Write a Python program to check if a number is prime using if_else. 



number = int(input("enter the number : "))
count = 0
for i in range(1,number+1):
    if number%i==0:
        count+=1
if count==2:
    print("number",number,"is prime")
else : 
    print("number",number,"is not prime")