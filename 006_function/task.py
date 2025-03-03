# from functools import reduce

# data = (0,1,5,6,8,9,36,71,81,95,26,51)
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
    
# k = reduce(max,data)
# print(k)


i = ["python","java","php","android"]
# def start(a):
#     if a[0]=='p':
#         return a
k = filter(lambda j:j.startswith('p'),i)
print(list(k))