
import BANKER as b
import CUSTOMER as c

choice = 0
print("""
      ========== Welcome To Banking App ==========
      """)

while choice != 3:
    print("""
        1. BANKER
        2. CUSTOMER
        3. EXIT  
        """)

    choice = int(input("Enter The Choice : "))

    if choice==1:
        c1 = 0
        
        print("""
            ========== Wellcome To Banker Section ==========
            """)
        
        while c1!=3:
            print("""
                1. Register
                2. Login
                3. Exit
                """)
            
            c1 = int(input("Enter choice : "))
            
            if c1==1:
                b.register()

            elif c1==2:
                b.login()

            elif c1==3:
                print("""
                    ========== You Are Exit To Main Menu ==========
                    """)

            else : 
                print("""
                    Enter Valid Choice..
                    """)



    elif choice==2:
        c1 = 0
        
        print("""
            ========== Wellcome To Customer Section ==========
            """)
        
        while c1!=3:
            print("""
                1. Register
                2. Login
                3. Exit
                """)
            
            c1 = int(input("Enter choice : "))
            
            if c1==1:
                c.register()

            elif c1==2:
                c.login()

            elif c1==3:
                print("""
                    ========== You Are Exit To Main Menu ==========
                    """)

            else : 
                print("""
                    Enter Valid Choice..
                    """)

    elif choice==3:
        print("""
            ========== You Are Now Exit ==========
            """)

    else : 
        print("""
            Enter Valid Choice..
            """)