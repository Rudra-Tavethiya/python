#3 digigt armstrong number

for i in range(100,1000):
    sum=0
    og=i
    while i>0:
        rem=i%10
        sum=sum+(rem**3)
        i=i//10
    if sum==og:
        print(sum)