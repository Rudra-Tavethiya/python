# Write a Python program to search for a word in a string using re.search().



import re

email = input("enter email : ")

parrten = "^[A-Za-z0-9]+@[A-Za-z]+.[A-Za-z]+$"

r = re.search(parrten,email)

if r is None:
    print("invalid email address...")
else: 
    print("valid email address...")