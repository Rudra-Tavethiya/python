print("program starting....")

try:
    # ZeroDivisionError
    # a=10
    # b=a/0
    # print(a)

    # ValueError
    # a=int(input("enter : "))
    # print(a)

    # IndexError
    # l=[1,2,3]
    # print(l[5])

    # KeyError
    d = {"1":"python", "2":"java"}
    print(d["3"])


# except ZeroDivisionError as z:
#     print(z)
# except ValueError as v:
#     print(v)
# except IndexError as i:
#     print(i)
except Exception as z:
    print(z)

else:
    print("else calling....")

finally:
    print("always excute....")

print("program ened....")