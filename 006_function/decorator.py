def mul(func):
    def warp(*a):
        func(*a)
        sum=1
        for i in a:
            sum*=i
        print("multiplication is : ",sum)
    return warp


@mul
def result(a,b):
    print("multiplication calling......")


result(10,20)