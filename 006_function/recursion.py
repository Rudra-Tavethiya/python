# recursion :it is a tecnique in programming where a function calls itself in order to solve a prblem.

#       it is work in two part:

#           base case : this is the condition where the function stop calling itself
#           recursive case : this is the condition where the function calling itself



def call(a):
    print(a+1)
    a+=1
    if a<20:
        call(a)

call(15)