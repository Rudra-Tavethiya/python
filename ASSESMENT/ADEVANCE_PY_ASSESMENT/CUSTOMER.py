


class register:
    def __init__(self):
        uname = input("Enter Username : ")
        email = input("Enter Email : ")
        pasword = input("Enter Password : ")
        print("""
              ===== User Registration successfully =====
              """)

class login:
    amount = 0

    def __init__(self):
        email = input("Enter Emmmail : ")
        pasword = input("Enter Password : ")
        print("""
            ===== User Login successfully =====
            """)
        c2 = 0
        while c2!=4:
            print("""
                1. withdraw Amount
                2. Deposit Amount
                3. View Balance
                4. Exit
                """)
            
            c2 = int(input("Enter Choice : "))

            if c2==1:
                withdraw()

            elif c2==2:
                deposit()

            elif c2==3:
                balance()

            elif c2==4:
                print("""
                    ========== You Are Exit To CUSTOMER'S Main Menu ==========
                    """)

            else : 
                print("""
                    Enter Valid Choice..
                    """)
    


class withdraw(login):
    def __init__(self):
        amt = int(input("Enter amount to withdraw : "))
        (login.amount)-=amt

class deposit(login):
    def __init__(self):
        amt = int(input("Enter amount to deposite : "))
        (login.amount)+=amt

class balance(login):
    def __init__(self):
        print("balance : ",login.amount)