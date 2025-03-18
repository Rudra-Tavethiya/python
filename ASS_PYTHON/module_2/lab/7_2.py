# Write a Python program to merge two lists into one dictionary using a loop.



dict = {}
keys = ["name","age","cource"]
values = ["rudra","20","python"]
for i in range((len(keys))):
    dict[keys[i]]=values[i]
print(dict)