# Write a Python program to access values using dictionary keys.



dict = {"name":"rudra",
        "age":"20",
        "cource":"python"}

print("name : ",dict["name"])
print("age : ",dict["age"])
print("cource : ",dict["cource"])
print("city : ",dict.get("city", "surat"))