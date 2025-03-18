# Write a Python program to sort a list using both sort() and sorted().


list = ["apple", "cherry", "kiwi", "banana"]
print("befor sorting : ",list)
list.sort()
print("after sort method : ",list)
list = ["apple", "cherry", "kiwi", "banana"]
list2 = sorted(list)
print("after sorted list2 : ",list2)
print("after sorted method original list : ",list)