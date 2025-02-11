# *****
# *****
# *****
# *****
# *****

# lines = 5
# for j in range(lines):
#     for i in range(lines):
#         print("*",end="")
#     print()


# *
# **
# ***
# ****
# *****

# lines = 5
# for j in range(lines):
#     for i in range(j+1):
#         print("*",end="")
#     print()

# lines = 5
# stars = 1
# for i in range(lines):
#     for i in range(stars):
#         print("*",end="")
#     print()
#     stars+=1


# *****
# ****
# ***
# **
# *

# lines = 5
# stars = 5
# for i in range(lines):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1



#     *
#    **
#   ***
#  ****
# *****


# lines = 5
# stars = 1
# space = lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1
#     space-=1


# *****
#  ****
#   ***
#    **
#     *


# lines = 5
# stars = 5
# space = 0
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1
#     space+=1



#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# lines = 5
# stars = 1
# space = lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end=" ")
#     print()
#     stars+=1
#     space-=1



#     *
#    ***
#   *****
#  *******
# *********



# lines = 5
# stars = 1
# space = lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=2
#     space-=1



#   *
#  ***
# *****
#  ***
#   *

# lines = 3
# stars = 1
# space = lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=2
#     space-=1 
# lines = 3
# stars = 3
# space = 1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=2
#     space+=1


#   *
#  * *
# *   *
#  * *
#   *


lines = 3
stars = 1
space = lines-1
space2 = 0
for i in range(lines):
    for k in range(space):
        print(" ",end="")
    for j in range(stars):
        print("*",end="")
    for l in range(space2):
        print(" ",end="")
    if i!=0:
        print("*",end="")
    print()
    space-=1 
    space2+=1