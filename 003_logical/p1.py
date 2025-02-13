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

# lines = 5
# stars = 1
# space = lines-1
# mid=(lines//2)+1
# for i in range(1,lines+1):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#             print("*",end="")
#     print()
#     if i<mid:
#         stars+=2
#         space-=1
#     else :
#         stars-=2
#         space+=1



#   *
#  * *
# *   *
#  * *
#   *

# lines = 5
# stars = 1
# space = lines-1
# mid=(lines//2)+1
# for i in range(1,lines+1):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         if j==0 or j==stars-1:
#             print("*",end="")
#         else :
#             print(" ",end="")
#     print()
#     if i<mid:
#         stars+=2
#         space-=1
#     else :
#         stars-=2
#         space+=1


# *
# **
# * *
# **
# *

# lines = 5
# stars = 1
# space = lines-1
# mid=(lines//2)+1
# for i in range(1,lines+1):
#     for j in range(stars):
#         if j==0 or j==stars-1:
#             print("*",end="")
#         else :
#             print(" ",end="")
#     print()
#     if i<mid:
#         stars+=1
#     else :
#         stars-=1


# 1
# 12
# 123
# 1234
# 12345


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15


# fact=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(fact,end=" ")
#         fact+=1
#     print()


# 0
# 10
# 010
# 1010
# 01010


# for i in range(1,6):
#     for j in range(1,i+1):
#         print((i+j)%2,end="")
#     print()


# 0
# 01
# 010
# 0101
# 01010


# zero=0
# one=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(one,end="")
#         else:
#             print(zero,end="")
#     print()


# A
# BC
# DEF
# GHIJ
# KLMNO

char='A'
for i in range(1,6):
    for j in range(1,i+1):
        print(char,end="")
        char+=1
    print()