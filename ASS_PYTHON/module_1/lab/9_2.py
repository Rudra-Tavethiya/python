# Write a Python program that manipulates and prints strings using various string methods.




words = "i am From surat"

print(words.capitalize())
print(words.casefold())
print(len(words))
print(words.center(41,'*'))
print(words.count('a',0,7))
print(words.endswith('m',0,9))
print(words.startswith('a',2,5))
print(words.find('k',3,9))   #if not found, return -1
# print(words.index('k',3,9)) # if not found return valueError