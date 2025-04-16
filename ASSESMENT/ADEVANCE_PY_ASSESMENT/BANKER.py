

class register:
    def __init__(self):
        uname = input("Enter Username : ")
        email = input("Enter Email : ")
        pasword = input("Enter Password : ")
        print("""
              ===== User Registration successfully =====
              """)        


class login:
    def __init__(self):
        email = input("Enter Email : ")
        pasword = input("Enter Password : ")
        print("""
              ===== User Login successfully =====
              """)
        c3 = 0
        while c3!=4:
            print("""
                1. Update All Customer
                2. View All Customer
                3. Delete All customer
                4. Exit
                """)
            c3 = int(input("Enter Choice : "))

            if c3==1:
                uc()

            elif c3==2:
                vc()

            elif c3==3:
                dc()

            elif c3==4:
                print("""
                    ========== You Are Exit To BANKER'S Main Menu ==========
                    """)

            else : 
                print("""
                    Enter Valid Choice..
                    """)


class uc:
    def __init__(self):
        print("For Update Enter The Id Of User : ")
        uname = input("Enter New Username : ")
        email = input("Enter New Email : ")
        Password = input("Enter New Password : ")
        print("""
              ===== User Information Updated successfully =====
              """)

class vc:
    def __init__(self):
        print("""
              == Currently No Data Available ==""")

class dc:
    def __init__(self):
        id = input("For deleting Enter The User Id : ")

        print("""
              ARE YOU SURE !!
              YOU REALLY WANT TO DELETE THE DATA OF THIS USER...
              Type "y" for YES And "n" for NO
              """)
        de = input("Enter 'y' or 'n' :")
        if de == 'y' or de == 'Y':
            print("""
                  == User data Deleted Successfully ==
                  """)
        elif de == 'n' or de == 'N':
            print("""
                  == User data Will Be Safe ==
                  """)
        else : 
            print("Enter Valid Choice...")