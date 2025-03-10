# file = open("text.txt",'r')
# print(file.read())


# file = open("text.txt",'w')
# file.write("python programing")


# file = open("text.txt",'a')
# file.write("go to home")



# file = open("text.txt",'r')
# print(file.readline())
# print(file.readline())
# print(file.readline())


# file = open("text.txt",'r')
# while True:
#     p = file.readline()
#     print(p)
#     if not p:
#         break


# file = open("text.txt",'r')
# print(file.readlines())

# with open("text.txt",'r') as f:
#     p = f.read()
#     print(p)


# with open("TAX.webp",'rb') as f:
#     p = f.read()
#     print(p)

with open("home.txt",'w+') as f:
    f.write("welcome home")
    f.seek(0)
    print(f.read())