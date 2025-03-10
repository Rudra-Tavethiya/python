

def manage_options():
    con='y'
    while con!='n':

        print("""
              Fruit Market Manager

              1) Add Fruit Stock
              2) View Fruit Stock
              3) Update Fruit Store

        """)
    
        choice = int(input("Enter Your Choice : "))
    
        if choice==1:
            data = {}
            print("ADD FRUIT STOCK")
            f_name = input("Enter Fruit Name : ")
            f_qty = int(input("Enter Qty (in KG) : "))
            f_prise = int(input("Enter Prise : "))

            

            con = input("do you want to perform more operations : press y fro yes and pressn for no : ")
            if con=='y':
                print("fruit dara added to stock")
                pass
            elif con=='n':
                print("data added to stock")
                break
            else : 
                print("enter valid input !!!")

        elif choice==2:
            print("view fruit stock")