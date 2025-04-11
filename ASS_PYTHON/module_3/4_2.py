# Write a Python program to write multiple strings into a file.



file = open("demo.txt",'w')
file.write("text for demo!!!!\n")
file.write("new line!!\n")
file.write("new addes!!")

print(file.tell())
file.seek(16)
print(file.tell())

file.close()