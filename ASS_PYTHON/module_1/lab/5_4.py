# Practical Example 4: Print this pattern using nested for loop: 

# * 
# ** 
# *** 
# **** 
# *****



lines=5
stars=1
for i in range(lines):
    for j in range(stars):
        print("*",end="")
    print()
    stars+=1