import FRUIT_MANAGER as f
import CUSTOMER as c


print("""
      WELCOME TO FRUIT MARKET
            
        1) Manager
        2) Customer
      
        3) EXIT
""")

choice = int(input("Enter Your Role : "))

if choice==1:
    f.manage_options()
elif choice==2:
    c.customer_operation()
elif choice==3:
    print("""
          YOU ARE EXIT NOW
          """)
else:
    print("""
          Invalid Choice !!!
          """)
