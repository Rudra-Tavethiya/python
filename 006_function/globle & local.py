# types of variable : 

#     global variable : we can excess the variale globaly

#     local variable : we can use only localy. 
#                      for example, in function variable we can call variable as local variable
#                      we can change the local variable by using "global" keyword

a=20
def local():
    global a
    a=50
    print(a)