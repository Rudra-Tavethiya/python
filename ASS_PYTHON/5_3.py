# Practical Example 3: Write a Python program to find a specific string in the list using a simple 
# for loop and if condition. 



list1=['apple','banana','mango']
find='banana'
found=False
for i in list1:
    if i==find:
        found=True
        if found==True:
            break

if found==True:
    print(find,"is present in this list")
else:
    print(find,"is not present in this list")    