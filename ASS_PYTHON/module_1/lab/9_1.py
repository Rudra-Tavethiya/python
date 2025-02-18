# Write a Python program to demonstrate string slicing. 



text = "I am from surat"

print("First five characters : ",text[:5])                       # Slicing from start to index 4
print("Characters from index 2 to 6 : ",text[2:7])               # Slicing between specific indexes
print("Last five characters : ",text[-5:])                       # Slicing last 5 characters
print("String without first and last character : ",text[1:-1])   # Removing first and last character
print("Every second character : ",text[::2])                     # Slicing with step size of 2
print("Reversed string : ",text[::-1])                           # Reversing the string