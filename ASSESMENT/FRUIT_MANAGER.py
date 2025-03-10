

def manage_options():
    data = {}
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
            
            print("ADD FRUIT STOCK")
            f_name = input("Enter Fruit Name : ")
            f_qty = int(input("Enter Qty (in KG) : "))
            f_prise = int(input("Enter Prise : "))

            data.update({f_name:{"qty":f_qty,"prise":f_prise}})

            con = input("do you want to perform more operations : press y fro yes and press n for no : ")
            if con=='y':
                print("\nFRUIT DATA ADDED IN STOCK\n")
                pass
            elif con=='n':
                print("\nDATA ADDED IN STOCK\n")
                break
            else : 
                print("\nYOU ENTER INVALID INPUT!!!\n")
                break

        elif choice==2:
            print("view fruit stock")
            print(data)
            break