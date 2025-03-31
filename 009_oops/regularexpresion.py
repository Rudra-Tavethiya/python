

import re

# email = "rudra@gmail.com"
# p = "^[A-Za-z0-9]+@[a-z]+.[a-z]+$"

# r = re.match(p,email)
# if r is None:
#     print("Invalid Email...")
# else:
#     print("Valid Email...")


# number = "9316977670"
# p = "^[0-9]{10}$"
# r = re.match(p,number)
# if r is None:
#     print("Invalid Mobile Number...")
# else:
#     print("Valid Mobile Number...")



str = "rudra"
p = "^[A-Za-z]+$"
r = re.match(p,str)
if r is None:
    print("Invalid String...")
else:
    print("Valid String...")