

def manage_options():
    print("""
          Fruit Market Manager

          1) Add Fruit Stock
          2) View Fruit Stock
          3) Update Fruit Store

    """)
    
    choice = int(input("Enter Your Choice : "))
    con='y'
    while con!='n':
        if choice==1:
            print("ADD FRUIT STOCK")
            f_name = input("Enter Fruit Name : ")
            f_qty = int(input("Enter Qty (in KG) : "))
            f_prise = int(input("Enter Prise : "))
        
            con = input("do you want to perform more operations : press y fro yes and pressn for no : ")
            if con=='y':
                pass
            elif con=='n':
                print("data added to stock")
            else : 
                print("enter valid input !!!")